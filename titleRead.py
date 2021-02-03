from selenium import webdriver
from bs4 import BeautifulSoup


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

    def removeTags(self):
        self.titlesToText()
        for i in range(len(self.titles)):
            title = ''
            tag = False
            for j in range(len(self.titles[i])):
                if self.titles[i][j] == '(' or self.titles[i][j] == '[' or self.titles[i][j] == '|':
                    tag = True
                if not tag:
                    title += self.titles[i][j]
                if self.titles[i][j] == ')' or self.titles[i][j] == ']':
                    tag = False
            self.titles[i] = title.strip()

    def returnTitles(self):
        self.removeTags()
        return self.titles
