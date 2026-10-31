# The Fenn Collection

Halloween 2026 party game. Three pages, no build step:

| Page | Path | Who uses it |
|---|---|---|
| Phone archive | `/` | Guests (scan the QR code) |
| Gamemaster | `/gm/` | You, on your phone (password in PRIVATE-NOTES.txt) |
| TV board | `/tv/` | The PC connected to the TV |

Game state lives in Supabase (project "Hobson Karaoke", tables prefixed `halloween_`). The tables are locked: the public key can only
call the game's functions, answers and hints stay on the server, and the GM password is checked on the server.

## Run locally
1. Double-click `start.bat` (needs Python; it runs `serve.py`, a small server that supports the big video).
2. TV: double-click `start-tv.bat` (full-screen Chrome, sound allowed). Exit with Alt+F4. Or open http://localhost:8000/tv/ and press F for full screen.
3. Phones/GM test on your PC: http://localhost:8000/ and http://localhost:8000/gm/
   (A phone on your home Wi-Fi can use the address `serve.py` prints. Guests on cell data need the hosted version.)

## TV test panel
Open `/tv/` and press **T** for a test panel (switch modes, make the board spell something, play the knock). Local only.

## Folders
- `media/` (NOT uploaded, too big): `storm_video.webm`, `seance_ambience.mp3`. The TV page runs from your PC, so it finds them here.
- `audio/` (uploaded): doorbells and the song. The GM page plays these on your phone.
- `img/`: board and planchette.

## Put the phone site + GM page online (GitHub Pages)
```
git init
git add .
git commit -m "The Fenn Collection"
git branch -M main
gh repo create fenn-collection --public --source=. --push
```
Then on GitHub: repo Settings > Pages > Deploy from branch > `main` / root.
The site appears at `https://<your-username>.github.io/fenn-collection/` in a minute or two.
(No `gh`? Create an empty public repo on github.com, then `git remote add origin <url>` and `git push -u origin main`.)
`media/` and `private/` are in `.gitignore`, so the big files and the answer notes are not uploaded.
