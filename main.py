from selenium import webdriver

url = input("Url of the playlist: ")
browser = webdriver.Chrome()
browser.get(url)
