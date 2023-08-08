from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware
from CreatePost import CreatePost;
from SearchPost import SearchPost;
from AssertDB import AssertDB;
import json;
import uvicorn

app = FastAPI();
a_db = AssertDB("banco.db");

origins = [
    "https://teste-vite-9owap1e4x-erbert-gadelha.vercel.app",
    "https://teste-vite-tau.vercel.app"
]

app.add_middleware(
    CORSMiddleware,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_credentials=True,
    allow_origins=origins,
)


if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=7777);

@app.get('/search')
async def SearchTags(tags: str = Query(...)):
    resposta = a_db.searchForTags(tags.split(','));
    return {'resposta': resposta}

@app.get('/post')
async def GetPosts(ids):
    resposta = a_db.searchForPosts(ids.split(','));

    retorno = {};
    for post in resposta:
        retorno[post[0]] = {'user': post[1], 'title': post[2], 'body': post[3]};
    
    return retorno

@app.post('/post')
async def SetPost(data: dict):
    print(data);
    a_db.publishPost(data);
    
    return {'resposta': 'post concluido'}
    '''
    try:
        c_post.criaPost(data);
        c_post.commit();
        return {'resposta': 'post concluido'}
    except:
        return {'resposta': 'erro ao criar post'}'''
    

@app.get('/settle')
async def get_data():
    retorno = 'povoou o banco' if(a_db.settle()) else 'banco ja povoado';
    print(retorno)
    return retorno;

@app.get('/all')
async def get_data():
    #retorno = str(a_db.getAllPosts()).replace('), (', '\n').replace('(', '').replace(')', '');
    retorno = a_db.getAllPosts()
    print(retorno)
    return retorno
