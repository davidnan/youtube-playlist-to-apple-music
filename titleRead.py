from selenium import webdriver
from bs4 import BeautifulSoup
from pairTitleSinger import Pair


class TitleRead:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.titles = None

    def getContent(self):
        content = self.driver.page_source.encode('utf-8').strip()
        soup = BeautifulSoup(content, 'lxml')
        self.titles = soup.findAll('a', id='video-title')
        self.driver.quit()

    def titlesToText(self):
        self.getContent()
        for i in range(len(self.titles)):
            self.titles[i] = self.titles[i].text

    def leaveOnlyAuthorAndSongTitle(self):
        self.titlesToText()

    def returnTitles(self):
        self.leaveOnlyAuthorAndSongTitle()
        return self.titles

