from bs4 import BeautifulSoup
import requests

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
data=response.text
soup=BeautifulSoup(data,"html.parser")
datas=soup.find_all(class_="title")
movielist=[]
for data in datas:
    movie=data.getText()
    movie=movie
    movielist.append(movie)

movielist=movielist[::-1]

with open("Top_100_movies",mode="w",encoding="utf-8") as file:
    for movie in movielist[:100]:
        file.write(movie + "\n")

