import os
import requests

API_KEY = os.getenv("TMDB_API_KEY", "")

BASE_URL = "https://api.themoviedb.org/3/movie/"
IMAGE_URL = "https://image.tmdb.org/t/p/w500"


def fetch_poster(movie_id):
    if not API_KEY:
        return "https://via.placeholder.com/500x750?text=Set+TMDB+API+Key"

    try:
        url = f"{BASE_URL}{movie_id}?api_key={API_KEY}&language=en-US"

        response = requests.get(url, timeout=10)
        response.raise_for_status()

        data = response.json()

        poster_path = data.get("poster_path")

        if poster_path:
            return IMAGE_URL + poster_path
        else:
            return "https://via.placeholder.com/500x750?text=No+Poster"

    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return "https://via.placeholder.com/500x750?text=No+Poster"