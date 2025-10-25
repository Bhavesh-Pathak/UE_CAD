from fastapi import FastAPI, Request
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Mount static files directory
app.mount("/assets", StaticFiles(directory="assets"), name="assets")

@app.get("/")
def read_root(request: Request):
    return templates.TemplateResponse("index.html", {"request": request})

@app.post("/stub/generate")
async def generate_stub(spec: dict):
    """
    Generate a stub preview based on JSON spec.
    For now, returns a static URL based on spec.
    """
    # Placeholder logic: check if spec has "type" key
    asset_type = spec.get("type", "cube")  # default to cube
    if asset_type == "cube":
        preview_url = "/assets/cube.glb"
    elif asset_type == "chair":
        preview_url = "/assets/chair.glb"
    elif asset_type == "gear":
        preview_url = "/assets/gear.glb"
    elif asset_type == "room":
        preview_url = "/assets/room.glb"
    else:
        preview_url = "/assets/cube.glb"  # fallback

    return {"preview_url": preview_url}