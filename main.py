from titleRead import TitleRead
from songAdd import SongAdd
import time


if __name__ == '__main__':
    url = input("Url of the playlist: ")
    titleReader = TitleRead(url)
    titles = titleReader.returnTitles()
    for title in titles:
        print(title)
    playlistTitle = input(
        "A window will open, please sign in into your Apple Music account! Please enter the playlist title you want "
        "your songs to be placed in ")
    songAdder = SongAdd(playlistTitle)
    songAdder.windowChange()
    for title in titles:
        songAdder.addSong(title)
    songAdder.driver.quit()

