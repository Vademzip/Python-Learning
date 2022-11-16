# -*- coding: utf-8 -*-


from bs4 import BeautifulSoup

with open("blank/index.html") as file:
    src = file.read()  # Сохраняем внутренности файла в src

soup = BeautifulSoup(src, "lxml")

title = soup.title
print(title)
