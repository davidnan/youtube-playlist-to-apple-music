from selenium import webdriver


class TitleRead:
    def __init__(self, url):
        self.url = url
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.titles = None

    # Gets the song title
    def getContent(self):
        self.titles = self.driver.find_elements_by_id("video-title")

    # Gets all the song titles and puts them in an array
    def titlesToText(self):
        self.getContent()
        for i in range(len(self.titles)):
            self.titles[i] = self.titles[i].text
        self.driver.quit()

    # Tries to remove unnecessary elements from the song title
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
        while '' in self.titles:
            self.titles.remove('')

    def returnTitles(self):
        self.removeTags()
        return self.titles
