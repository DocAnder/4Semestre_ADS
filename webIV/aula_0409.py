from fastapi import FastAPI
import uvicorn
from datetime import datetime
import atividade_2808 as tmbd


app = FastAPI()

# ===================================================================

# ATIVIDADE 1
@app.get("/filme/{title}")
async def find_movie(title: str):
    """
    Procurar filmes pelo nome e ordenar pelos mais populares
    """
    data = tmbd.get_json(
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

  
# ===================================================================

# ATIVIDADE 2

@app.get("/artista/filmes")
async def get_movies_artist(artistId: int):
    """
    Busca os filmes mais populares de um artista (filtrar a lista por popularidade)
    """
    # URL --url 'https://api.themoviedb.org/3/person/person_id/movie_credits?language=en-US' \
    



@app.get("/artista/{name}")
async def get_artista(name: str):
    data = tmbd.get_json(
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
    uvicorn.run("aula_0409:app", host="127.0.0.1", port=8000, reload=True)
