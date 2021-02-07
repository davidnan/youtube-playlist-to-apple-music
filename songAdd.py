from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time


class SongAdd:
    def __init__(self, playlist_title):
        self.playlist_title = playlist_title
        self.url = 'https://music.apple.com/login'
        self.driver = webdriver.Chrome()
        self.driver.get(self.url)
        self.searchBar = None
        self.playlist_found = False

    def windowChange(self):
        flag = True
        while flag:
            if self.driver.current_url != self.url:
                flag = False
        print("Logged in successfully")
        self.searchBar = self.driver.find_element_by_xpath("html/body/div[3]/nav/div[2]/div/input")

    def searchSong(self, title):
        self.searchBar.send_keys(title)
        self.searchBar.send_keys(Keys.RETURN)
        self.searchBar.clear()

    def findSongOnPage(self, title):
        self.searchSong(title)
        actions = ActionChains(self.driver)
        time.sleep(5)
        song = self.driver.find_element_by_xpath("html/body/div[3]/div[1]/div[5]/div/div[2]/div/div[2]/div/div")
        actions.move_to_element(song)
        actions.perform()
        time.sleep(1)
        song_menu = self.driver.find_element_by_class_name("action-menu")
        song_menu.click()

    def addSong(self, title):
        self.findSongOnPage(title)
        playlist_menu = self.driver.find_element_by_xpath("html/body/div[4]/ul/li/span")
        playlist_menu.click()
        playlists = self.driver.find_element_by_xpath("html/body/div[4]/ul/li/div/ul")
        options = playlists.find_elements_by_tag_name("li")
        for option in options:
            if option.text == self.playlist_title:
                option.click()
                if not self.playlist_found:
                    print("Playlist found!")
                self.playlist_found = True
                break
        if not self.playlist_found:
            print("Playlist was not found")
            self.driver.quit()

