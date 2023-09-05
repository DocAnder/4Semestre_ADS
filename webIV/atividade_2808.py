import requests
from fastapi import FastAPI
import uvicorn


api_key = "eadfd7b3ad42cd212ffdbc024eddca05"

genres = [
    {'id': 28, 'name': 'Action'},
    {'id': 12, 'name': 'Adventure'},
    {'id': 16, 'name': 'Animation'},
    {'id': 35, 'name': 'Comedy'}, {'id': 80, 'name': 'Crime'}, {'id': 99, 'name': 'Documentary'},
    {'id': 18, 'name': 'Drama'}, {'id': 10751, 'name': 'Family'}, {'id': 14, 'name': 'Fantasy'},
    {'id': 36, 'name': 'History'}, {'id': 27, 'name': 'Horror'}, {'id': 10402, 'name': 'Music'},
    {'id': 9648, 'name': 'Mystery'}, {'id': 10749, 'name': 'Romance'}, {'id': 878, 'name': 'Science Fiction'},
    {'id': 10770, 'name': 'TV Movie'}, {'id': 53, 'name': 'Thriller'}, {'id': 10752, 'name': 'War'},
    {'id': 37, 'name': 'Western'}]


def get_json(endpoint, params=None):
    """
    fornecido o endpoint faz o request e retorna o resultado em json
    """
    url = f"{endpoint}{params}&api_key={api_key}"
    response = requests.get(url)
    return response.json()


# 1) IMPLEMENTAR USANDO REQUESTS DO PYTHON:

# A) BUSCAR NOME DO GENERO FORNECIDO O ID
def get_genero_id(id_genre: int):
    for genre in genres:
        if genre['id'] == id_genre:
            # print(id, genre['name'])
            return genre['name']
    return None


# ====================================


# B) BUSCAR UM FILME PELO TITULO
def get_movie_by_name(name: str):
    data = get_json(
        "https://api.themoviedb.org/3/search/movie",
        f"?query={name}"
    )
    print(data)
    return data


# ====================================


# C) BUSCAR ARTISTA PELO NOME
def get_artist_by_name(name: str):
    data = get_json(
        "https://api.themoviedb.org/3/search/person",
        f"?query={name}"
    )
    return data

 
# ====================================


def get_artist_by_id(id: int):
    data = get_json(
        "https://api.themoviedb.org/3/person/",
        f"{id}"
        )


# IMPLEMENTAR API USANDO FASTAPI:

# ENDPOINT QUE RETORNA 5 FILMES RECOMENDADOS DA SEMANA

app = FastAPI()


@app.get('/week')
def get_week_movies():
    data = get_json(
        "https://api.themoviedb.org/3/trending/movie/week?language=en-US"
        "?"
    )
    five_movies = []
    for movie in data['results']:
        five_movies.append(movie)
        if len(five_movies) == 5:
            break
    return five_movies


if __name__ == "__main__":
    # print(get_genero_id(12))
    #print(get_movie_by_name('avatar'))
    # print(get_artist_by_name("arnold"))
    # print(get_five_recommended())
    #uvicorn.run("atividade_2808:app", host="127.0.0.1", port=8000, reload=True)
    print(get_artist_by_id(50))
