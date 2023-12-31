from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
import json;
import uvicorn

from src.api.search import router as search_router
from src.api.post import router as post_router

app = FastAPI();

origins = [
    "https://teste-vite-9owap1e4x-erbert-gadelha.vercel.app",
]

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=origins,
)

app.include_router(search_router, prefix="/search", tags=["search"])
app.include_router(post_router, prefix="/post", tags=["post"])

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777);

@app.get('/')
async def SearchTags():
    return {'resposta': 'Bem Vindo!'}
