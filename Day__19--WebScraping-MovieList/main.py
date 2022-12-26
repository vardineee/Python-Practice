import requests
from bs4 import BeautifulSoup


URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")
movies = soup.find_all(name="h3", class_="title")

movies_title = [ movie.getText() for movie in movies]


all_movies = movies_title[::-1]

with open("movies.txt", mode="w") as file:
    for movie_item in all_movies:
        file.write(f"{movie_item}\n")
