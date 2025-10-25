# UE_CAD Stub

A small FastAPI-based stub service and static viewer for previewing simple CAD/UE assets.

This repository provides a minimal backend and frontend to demonstrate how an asset-spec JSON can be converted to a preview URL and displayed in a browser using a Three.js viewer.

## What this is

- A FastAPI application (`main.py`) that serves a simple HTML viewer and a single POST endpoint `/stub/generate` which returns a `preview_url` for a requested asset type.
- A static `templates/index.html` frontend that uses Three.js to fetch the preview URL and load a `.glb` model into a WebGL viewer.
- An `assets/` folder with placeholder files (currently `.txt` placeholders). Replace these with real `.glb` files named `cube.glb`, `chair.glb`, `gear.glb`, `room.glb` for the demo viewer to load them.

## Project structure

- `main.py` — FastAPI application. Serves templates and static assets; implements `/stub/generate`.
- `run.bat` — Windows helper that runs the app with the venv python (if a `venv` exists).
- `templates/index.html` — Frontend viewer (Three.js + GLTFLoader + OrbitControls).
- `assets/` — Static assets (placeholders). The viewer expects `.glb` files here.
- `docs/api_formats.md` — API contract for `/stub/generate`.

## Quick start (Windows)

1. Open PowerShell and change into the project folder:

   ```powershell
   cd "c:\Users\pc45\Desktop\Desktop Folder\UE_CAD\ue_cad_stub"
   ```

2. Create a virtual environment (if you don't have one) and activate it:

   ```powershell
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Install dependencies:

   ```powershell
   pip install fastapi uvicorn jinja2 aiofiles
   ```

   (There is no `requirements.txt` in this stub; the above installs the minimum packages needed.)

4. Run the server:

   - Option A: Use the helper batch file (from PowerShell):

     ```powershell
     .\run.bat
     ```

   - Option B: Run Uvicorn directly (recommended during development):

     ```powershell
     python -m uvicorn main:app --reload --host 127.0.0.1 --port 8000
     ```

5. Open your browser to `http://127.0.0.1:8000`.

6. In the viewer page, type one of: `cube`, `chair`, `gear`, `room` and click "Show Asset".

## API: `/stub/generate`

See `docs/api_formats.md` for details. In short:

- Method: POST
- Body: JSON { "type": "cube" | "chair" | "gear" | "room" }
- Response: JSON { "preview_url": "/assets/<name>.glb" }

Example (curl):

```powershell
curl -X POST "http://127.0.0.1:8000/stub/generate" -H "Content-Type: application/json" -d '{"type":"gear"}'
```

Expected response:

```json
{"preview_url":"/assets/gear.glb"}
```

## Important notes & troubleshooting

- Asset placeholders: The repository's `assets/` folder currently contains human-readable `.txt` placeholders. The viewer expects `.glb` files at paths such as `/assets/cube.glb`. To see actual models, place `.glb` files in `assets/` with the expected names.
- If the viewer shows "Error loading GLB" or the network console reports 404 when loading `/assets/*.glb`, confirm the `.glb` files exist in the `assets` folder.
- Static files serving: FastAPI's `StaticFiles` is used to serve `assets/`. If you add large files, performance depends on the deployment. For production, serve static assets from a dedicated static file server or CDN.
- Ports and host: The default bind is `127.0.0.1:8000`. If you need external access, change `--host` and firewall rules appropriately.

## Extending the stub

- Add real GLB exports from your CAD tool into `assets/` and keep names consistent.
- Expand `main.py` to perform real generation/conversion of CAD assets, or to validate spec properties beyond the current `type` summary.
- Add authentication or rate-limiting if you expose the service publicly.

## How I validated this README

- I inspected `main.py`, `templates/index.html`, `docs/api_formats.md`, `run.bat` and the `assets/` placeholders to capture behavior and current gaps (notably missing `.glb` files).

---

If you want, I can also:
- Add a `requirements.txt` (or `pyproject.toml`) and a simple test that checks `/stub/generate` returns expected preview URLs.
- Attempt to push this README to the GitHub repo you provided. (Note: pushing will require that your local git is configured with permissions to push to that repository; if the push fails due to authentication, I'll show the exact git commands to run locally.)

Enjoy — tell me if you'd like a `requirements.txt` and a tiny unit test next.
