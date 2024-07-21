from bs4 import BeautifulSoup
import requests


response = requests.get("https://www.empireonline.com/movies/features/best-movies-2/")
empire_web_page = response.text

soup = BeautifulSoup(empire_web_page, "html.parser")
movie_names = soup.find_all(name="h3")
movies = []
for name in movie_names:
    movies.append(name.text)

movies.reverse()

with open("100_movies_of_all_time.txt", "w") as movie_file:
    for movie in movies:
        movie_file.write(f"{movie}\n")
