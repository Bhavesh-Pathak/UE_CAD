import sys
import os
from fastapi.testclient import TestClient

# Ensure project root is on sys.path so tests can import main.py
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
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
