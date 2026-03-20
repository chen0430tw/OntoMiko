from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routers.divine import router as divine_router

app = FastAPI(title="OntoMiko API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(divine_router)

@app.get("/health")
def health():
    return {"status": "ok"}
