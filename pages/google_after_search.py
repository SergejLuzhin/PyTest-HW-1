from selenium.webdriver.common.by import By


class GoogleAfterSearch:
    python_link_locator = (By.XPATH, "//a[contains(@href, 'wikipedia')]//h3[text() = 'Python']")

    # (//a//h3)[1]

    def __init__(self, webdriver):
        self.webdriver = webdriver

    def open_link_with_number(self, link_number: int):
        link_locator = (By.XPATH, f"(//a//h3)[{link_number}]")
        self.webdriver.find_element(*self.python_link_locator).click()

    def open_link_with_site_and_title(self, site: str, title: str):
        link_locator = (By.XPATH, f"//a[contains(@href, '{site}')]//h3[text() = '{title}']")
        self.webdriver.find_element(*self.python_link_locator).click()