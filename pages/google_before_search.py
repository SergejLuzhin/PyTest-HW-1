import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class GoogleBeforeSearch:
    search_input_locator = (By.NAME, "q")

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def search(self, query: str):
        time.sleep(3) #пауза чтобы закрыть всплывающее окно
        search_input = self.webdriver.find_element(*self.search_input_locator)
        search_input.send_keys(query, Keys.ENTER)