from titleRead import TitleRead

if __name__ == '__main__':
    url = input("Url of the playlist: ")
    titleReader = TitleRead(url)
    titles = titleReader.returnTitles()
    for title in titles:
        print(title)

