from fastapi import APIRouter, Query
from src.db.server import server_;
import json;

router = APIRouter()

@router.get('/')
async def search(id: str = Query(None), ids: str = Query(None)):

    retorno = {};

    if id is not None:
        post = server_.searchForPosts([id])[0]
        retorno = {id: {'user': post[1], 'title': post[2], 'body': post[3]}};
    elif ids is not None:
        resposta = server_.searchForPosts(ids.split(','))
        for post in resposta:
            retorno[post[0]] = {'user': post[1], 'title': post[2], 'body': post[3]};
    else:
        return {'None': 'Bem Vindo aos Posts!'}
    
    if len(retorno) == 0:
        return 'not found'
    else:
        return retorno