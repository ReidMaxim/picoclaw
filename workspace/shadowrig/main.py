# SHADOWRIG — PHASE 1
# FastAPI application skeleton

from fastapi import FastAPI, Request, HTTPException, UploadFile, File
from fastapi.responses import HTMLResponse, JSONResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
import uvicorn
import os

app = FastAPI(title="ShadowRig", version="0.1.0")

# CORS for frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")


@app.get("/", response_class=HTMLResponse)
async def desktop():
    """Serve the VoidTerminal desktop interface."""
    with open("app/static/index.html", "r") as f:
        return f.read()


@app.post("/api/upload")
async def upload_wardrive_data(file: UploadFile = File(...)):
    """
    Upload wardriving data (CSV/JSON).
    Phase 2 will implement parsing and database storage.
    """
    content = await file.read()
    # Placeholder: return success with basic info
    return {
        "status": "received",
        "filename": file.filename,
        "size": len(content),
        "message": "Upload endpoint ready for Phase 2 implementation."
    }


@app.get("/api/map")
async def get_map_data():
    """
    Return all AccessPoints and Zones for map rendering.
    Phase 2 will implement actual database queries.
    """
    return {
        "access_points": [],  # TODO: query DB
        "zones": []  # TODO: query DB
    }


# Health check
@app.get("/health")
async def health():
    return {"status": "ok", "service": "ShadowRig"}


if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )