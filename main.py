from selenium import webdriver
from bs4 import BeautifulSoup
from titleRead import TitleRead

url = input("Url of the playlist: ")

if __name__ == '__main__':
    titleReader = TitleRead(url)
    titles = titleReader.getContent()
    for title in titles:
        print(title.text)

