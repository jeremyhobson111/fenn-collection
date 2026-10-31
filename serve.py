"""Tiny local web server with HTTP Range support (needed for the big storm video).
Run:  py serve.py   (or double-click start.bat).  Then open http://localhost:8000/tv/
"""
import http.server, socketserver, os, re, socket, sys

PORT = int(os.environ.get('PORT', '8000'))
os.chdir(os.path.dirname(os.path.abspath(__file__)))

class H(http.server.SimpleHTTPRequestHandler):
    extensions_map = {**http.server.SimpleHTTPRequestHandler.extensions_map, '.webm': 'video/webm', '.mp3': 'audio/mpeg', '.mjs': 'text/javascript'}
    def end_headers(self):
        self.send_header('Accept-Ranges', 'bytes'); self.send_header('Cache-Control', 'no-cache'); super().end_headers()
    def send_head(self):
        rng = self.headers.get('Range'); path = self.translate_path(self.path)
        self._remaining = None
        if not rng or os.path.isdir(path) or not os.path.exists(path):
            return super().send_head()
        m = re.match(r'bytes=(\d*)-(\d*)', rng)
        if not m or (not m.group(1) and not m.group(2)):
            return super().send_head()
        f = open(path, 'rb'); size = os.fstat(f.fileno()).st_size
        if m.group(1):
            start = int(m.group(1)); end = int(m.group(2)) if m.group(2) else size - 1
        else:
            start = max(0, size - int(m.group(2))); end = size - 1
        end = min(end, size - 1)
        if start > end or start >= size:
            f.close(); self.send_response(416); self.send_header('Content-Range', f'bytes */{size}'); self.end_headers(); return None
        self.send_response(206)
        self.send_header('Content-Type', self.guess_type(path)); self.send_header('Content-Range', f'bytes {start}-{end}/{size}')
        self.send_header('Content-Length', str(end - start + 1)); self.end_headers()
        f.seek(start); self._remaining = end - start + 1
        return f
    def copyfile(self, src, dst):
        try:
            if self._remaining is None:
                return super().copyfile(src, dst)
            left = self._remaining
            while left > 0:
                chunk = src.read(min(1 << 20, left))
                if not chunk: break
                dst.write(chunk); left -= len(chunk)
        except (BrokenPipeError, ConnectionResetError, ConnectionAbortedError):
            pass
    def log_message(self, fmt, *a):
        if '/rest/' not in self.path and not self.path.endswith(('.mp3', '.webm')): super().log_message(fmt, *a)

class S(socketserver.ThreadingMixIn, http.server.HTTPServer):
    daemon_threads = True

def lan_ip():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM); s.connect(('8.8.8.8', 80)); ip = s.getsockname()[0]; s.close(); return ip
    except Exception: return 'your-pc-ip'

if __name__ == '__main__':
    print(f'\n  The Fenn Collection - local server\n  TV page:    http://localhost:{PORT}/tv/\n  Phone site: http://localhost:{PORT}/   (same Wi-Fi: http://{lan_ip()}:{PORT}/)\n  GM page:    http://localhost:{PORT}/gm/\n  Press Ctrl+C to stop.\n')
    try: S(('0.0.0.0', PORT), H).serve_forever()
    except KeyboardInterrupt: sys.exit(0)
