import time

import allure
import pytest
from selenium.webdriver.common.by import By

from conf.config import *
from conftest import chromedriver
from pages.google_after_search import GoogleAfterSearch
from pages.google_before_search import GoogleBeforeSearch
from pages.wikipedia_page import WikipediaPage
from utils.test_utils import allure_screenshot


@pytest.fixture(scope="package")
def webdriver(chromedriver):
    chromedriver.get(google_url)
    return chromedriver

@pytest.mark.ui_test
@allure.epic("Сайт google.com")
@allure.feature("Тест поиска")
@allure.title("Проверка поиска google и википедии")
def test_google(webdriver):
    with allure.step("Перейти по ссылке: https://www.google.com/"):
        google_before_search = GoogleBeforeSearch(webdriver)
        assert webdriver.title == "Google", "Заголовок вкладки некорректный"

    with allure.step("Ввести в строку поиска «Python википедия». Нажать поиск."):
        google_before_search.search("Python википедия")
        time.sleep(15) ##ввод капчи

    with allure.step("Открыть первую страницу Вики в выдаче поиска с материалом про Python"):
        google_after_search = GoogleAfterSearch(webdriver)
        elements = webdriver.find_elements(By.XPATH, "//div/span[contains(. , 'wikipedia')]")
        assert len(elements) > 0, "Ссылок на 'wikipedia' не найдено на странице"
        google_after_search.open_link_with_site_and_title("wikipedia", "Python")
        assert "Python".lower() in webdriver.title.lower(), "Заголовок вкладки не содержит 'Python'"

    with allure.step("Проверить в инфо-карточке Python сведения под заголовком автор"):
        wikipedia_page = WikipediaPage(webdriver)
        assert wikipedia_page.get_author_in_table() == "Гвидо ван Россум"

