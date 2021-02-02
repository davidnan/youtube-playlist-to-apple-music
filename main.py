from titleRead import TitleRead

url = input("Url of the playlist: ")

if __name__ == '__main__':
    titleReader = TitleRead(url)
    titles = titleReader.returnTitles()
    for title in titles:
        print(title)

