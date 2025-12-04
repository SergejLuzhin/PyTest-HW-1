from selenium.webdriver.common.by import By


class WikipediaPage:
    def __init__(self, webdriver):
        self.webdriver = webdriver

# //tr[th[contains(. , 'Автор')]]//span/a
    def get_author_in_table(self) -> str:
        return self.webdriver.find_element(By.XPATH, "//tr[th[contains(. , 'Автор')]]//span/a").text