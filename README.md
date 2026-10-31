# The Fenn Collection

Halloween 2026 party game. Three pages, no build step. Everything lives in `fenn-collection/` so the live site is
`https://hobsonhalloween.com/fenn-collection/` and the domain root stays a quiet placeholder.

| Page | Path | Who uses it |
|---|---|---|
| Phone archive | `/fenn-collection/` | Guests (scan the QR code) |
| Gamemaster | `/fenn-collection/gm/` | You, on your phone (password in PRIVATE-NOTES.txt) |
| TV board | `/fenn-collection/tv/` | The PC connected to the TV |

Game state lives in Supabase (project "Hobson Karaoke", tables prefixed `halloween_`). The tables are locked: the public key can only
call the game's functions, answers and hints stay on the server, and the GM password is checked on the server.

## Run locally
1. Double-click `start.bat` (needs Python; runs `serve.py`, a small server that supports the big video).
2. TV: double-click `start-tv.bat` (full-screen Chrome, sound allowed). Exit with Alt+F4. Or open http://localhost:8000/fenn-collection/tv/ and press F.
3. Test on your PC: http://localhost:8000/fenn-collection/ and http://localhost:8000/fenn-collection/gm/

## TV test panel
Open the TV page and press **T** (local only): switch modes, make the board spell something, play the knock.

## Folders
- `media/` (NOT uploaded, too big; sits next to `fenn-collection/`): `storm_video.webm`, `seance_ambience.mp3`.
- `fenn-collection/audio/` (uploaded): doorbells, song, knock. The GM page plays these on your phone.
- `private/` (NOT uploaded): story text and printable sheets.

## Publishing changes
```
git add -A
git commit -m "update"
git push
```
GitHub Pages rebuilds in a minute or two. `media/` and `private/` are in `.gitignore`.
