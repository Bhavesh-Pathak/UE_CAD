from fastapi.testclient import TestClient
from main import app


def test_generate_stub_cube():
    client = TestClient(app)
    resp = client.post("/stub/generate", json={"type": "cube"})
    assert resp.status_code == 200
    data = resp.json()
    assert "preview_url" in data
    assert data["preview_url"].endswith("/cube.glb")


def test_generate_stub_unknown_defaults_to_cube():
    client = TestClient(app)
    resp = client.post("/stub/generate", json={"type": "unknown"})
    assert resp.status_code == 200
    data = resp.json()
    assert data["preview_url"].endswith("/cube.glb")
