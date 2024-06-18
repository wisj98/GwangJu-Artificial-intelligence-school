import requests
import time

import openpyxl as xl

from matplotlib import font_manager, rc
import matplotlib.pyplot as plt

import pandas as pd


font_path = "C:/Windows/Fonts/malgun.ttf" 
font = font_manager.FontProperties(fname = font_path).get_name()
rc('font', family = font)

api_key = "a1232fe9acbc1e835c06033ecaa83080"

genre_dict = {28:"action",12:"adventure",16:"animation",35:"comedy",80:"crime",99:"documentary",18:"drama",10751:"family",14:"fantasy",
              36:"history",27:"horror",10402:"music",9648:"mystery",10749:"romance",878:"science fiction",10770:"tv movie",
              53:"thriller",10752:"war",37:"western"}

score_by_genre = {}
for genre in genre_dict.keys():
    scores = 0
    count = 0
    for i in range(1,11):
        url = f"https://api.themoviedb.org/3/discover/movie?api_key={api_key}&with_genres={genre}&page={i}"
        response = requests.get(url)
        data = response.json()
        for j in data["results"]:
            scores += j["vote_average"]
            count += 1
    score_by_genre[genre_dict[genre]] = round(scores / count, 2)
    print(f"{genre_dict[genre]} done")

print(url)
print(score_by_genre)

score_by_genre = dict(sorted(score_by_genre.items(), key=lambda item:item[1]))

plt.figure(figsize=(10, 6))
plt.bar(score_by_genre.keys(), [score_by_genre[i] for i in score_by_genre.keys()])
plt.xlabel("Genre")
plt.ylabel("Vote Average")
plt.title(" Movies Vote Average")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.show()

import streamlit as st
st.pyplot(plt)