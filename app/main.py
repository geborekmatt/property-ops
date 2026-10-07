from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

app = FastAPI(title="PropertyOps")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://127.0.0.1:5173", "http://localhost:5173"],
    allow_methods=["GET"],
    allow_headers=[],
)


class Health(BaseModel):
    status: str


@app.get("/health", response_model=Health)
async def health() -> Health:
    return Health(status="ok")
