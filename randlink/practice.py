import webbrowser
import random

with open("songs.txt", "r") as file:
    urls = file.read().splitlines()

for url in urls :
    webbrowser.open(url)