from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.dnsdist_client import fetch_all_top_queries
from app.config import DNSDIST_SERVERS

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/api/top-queries")
def get_top_queries():
    return fetch_all_top_queries(DNSDIST_SERVERS)
