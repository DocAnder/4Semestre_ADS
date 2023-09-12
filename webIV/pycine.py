from fastapi import FastAPI
import uvicorn
from datetime import datetime
from atividade_2808 import get_json

app = FastAPI()

from fastapi.middleware.cors import (
     CORSMiddleware
)
# habilita CORS (permite que o Svelte acesse o fastapi)
origins = [
    "http://localhost",
    "http://localhost:5174",
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/filme/{title}")
async def find_movie(title: str):
    """
    Procurar filmes pelo nome e ordenar pelos mais populares
    """
    data = get_json(
      "https://api.themoviedb.org/3/search/movie",
        f"?query={title}"  
    )
    result = data['results']
    filtro: list = []
    for movie in result:
        filtro.append({
            'id': movie['id'],
            'title': movie['title'],
            'rank': movie['popularity']
        })
    filtro.sort(reverse=True,key=lambda artist: artist['rank'])
    return filtro


@app.get("/artista/filmes")
async def get_movies_artist(artistId: int):
    """
    Busca os filmes mais populares de um artista (filtrar a lista por popularidade)
    """
    data = tmbd.get_json(
        f"https://api.themoviedb.org/3/person/{person_id}/movie_credits?language=en-US"
    )
    filtro: list = []
    result = data['cast']
    for movie in result:
        filtro.append({
            'id': movie['id'],
            'title': movie['title'],
            'popularity': movie['popularity']
        })
    filtro.sort(reverse=True,key=lambda movie: movie['polularity'])
    return filtro

    



@app.get("/artista/{name}")
async def get_artista(name: str):
    data = get_json(
      "https://api.themoviedb.org/3/search/person",
        f"?query={name}"  
    )
    result = data['results']
    filtro: list = []
    for artist in result:
        filtro.append({
            'id': artist['id'],
            'artist': artist['name'],
            'rank': artist['popularity']
        })
    filtro.sort(reverse=True,key=lambda artist: artist['rank'])
    return filtro




if __name__ == "__main__":
    uvicorn.run("pycine:app", host="127.0.0.1", port=8000, reload=True) 