@echo off
rem Opens the TV page full-screen in its own Chrome window (sound allowed without clicking).
rem Exit with Alt+F4. Start start.bat first.
set URL=http://localhost:8000/fenn-collection/tv/
set FLAGS=--kiosk --autoplay-policy=no-user-gesture-required --user-data-dir="%TEMP%\hw_tv_profile" --no-first-run --disable-session-crashed-bubble
if exist "C:\Program Files\Google\Chrome\Application\chrome.exe" ( start "" "C:\Program Files\Google\Chrome\Application\chrome.exe" %FLAGS% %URL% & exit /b )
if exist "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" ( start "" "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe" %FLAGS% %URL% & exit /b )
start "" msedge --kiosk %URL% --edge-kiosk-type=fullscreen --autoplay-policy=no-user-gesture-required --user-data-dir="%TEMP%\hw_tv_profile"
