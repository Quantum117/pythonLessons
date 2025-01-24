import requests

API_KEY = '60a71aee7d0b5ffe1ff4d67f09a57e0a'

# Base URL for TMDB
BASE_URL = "https://api.themoviedb.org/3/discover/movie"


url = "https://api.themoviedb.org/3/discover/movie?include_adult=false&include_video=false&language=en-US&page=1&sort_by=popularity.desc"

headers = {
    "accept": "application/json",
    "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI2MGE3MWFlZTdkMGI1ZmZlMWZmNGQ2N2YwOWE1N2UwYSIsIm5iZiI6MTczNzY1MDA2Ny43MjUsInN1YiI6IjY3OTI2ZjkzNDJmNDU5ZDg0MzkyMDU4YiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.W6buWsQIsq18wvD1h8UFiC9-1BtEieA6LKF-iE0v1EI"
}

response = requests.get(url, headers=headers)

# print(response.text)

url = "https://api.themoviedb.org/3/genre/movie/list?language=en"


data = requests.get(url, headers=headers).json()
# Extract genre names
genre_names = [genre["name"] for genre in data["genres"]]
genre_ids = [genre["id"] for genre in data["genres"]]

data_dict = dict(zip(genre_names,genre_ids))
print("Movie genres: ")

# Show all movie genres
for name in genre_names:
   print(name)
name = input("please enter movie genre :").strip()

if name in genre_names:
    movie_id = data_dict[f'{name}']
    print(movie_id)
    # Parameters for the request
    params = {
        "api_key": API_KEY,
        "with_genres": movie_id,  # Action genre ID
        "language": "en-US",
        "sort_by": "popularity.desc"
    }

    # Send GET request
    response = requests.get(BASE_URL, params=params)

    # Check if request was successful
    if response.status_code == 200:
        # Parse JSON response
        data = response.json()
        movies = data["results"]
        for movie in movies:
            print(f"Title: {movie['title']}, Release Date: {movie['release_date']}")
    else:
        print(f"Failed to fetch data. Status code: {response.status_code}")
else:
    print("Movie genre is not in the list ")