import time
import allure
import pytest

from conf.config import *
from conftest import chromedriver
from pages.google_after_search import GoogleAfterSearch
from pages.google_before_search import GoogleBeforeSearch
from pages.wikipedia_page import WikipediaPage
from utils.data_provider import *


@pytest.fixture(scope="package")
def webdriver(chromedriver):
    """Инициализирует и возвращает экземпляр WebDriver для выполнения тестов.

        Назначение:
            Открывает главную страницу Google перед выполнением тестового сценария
            и предоставляет настроенный браузер в тестовые функции.

        Параметры:
            chromedriver: Фикстура, создающая экземпляр WebDriver.

        Возвращает:
            WebDriver: объект управляемого браузера.

        Автор: Сергей Лужин
        """
    chromedriver.get(google_url)
    return chromedriver

@pytest.mark.ui_test
@allure.epic("Сайт google.com")
@allure.feature("Тест поиска")
@allure.title("Проверка поиска google и википедии")
@pytest.mark.parametrize("query, needed_site, needed_title, checked_author", data_provider_for_google_search_test())
def test_google_search(webdriver, query: str, needed_site: str, needed_title: str, checked_author: str):
    """Тест проверяет корректность поиска в Google и информации на странице Wikipedia.

        Назначение:
            1. Проверить доступность главной страницы Google.
            2. Выполнить поиск по запросу.
            3. Убедиться, что в результатах поиска присутствует ссылка на целевой сайт.
            4. Перейти по найденной ссылке на страницу Wikipedia.
            5. Проверить корректность заголовка страницы Wikipedia.
            6. Проверить корректного автора в информационной таблице статьи.

        Параметры:
            webdriver: Экземпляр Selenium WebDriver, передаваемый фикстурой.
            query (str): Поисковый запрос, который вводится в Google.
            needed_site (str): Домен целевого сайта, присутствующий в результатах поиска.
            needed_title (str): Текст заголовка страницы, которую необходимо открыть.
            checked_author (str): Ожидаемое имя автора в информационной таблице Wikipedia.

        Автор: Сергей Лужин
        """
    with allure.step("Перейти по ссылке: https://www.google.com/"):
        google_before_search = GoogleBeforeSearch(webdriver)
        google_before_search.check_title()
        time.sleep(3)  # пауза чтобы закрыть всплывающее окно

    with allure.step(f"Ввести в строку поиска «{query}». Нажать поиск."):
        google_before_search.search(query)
        time.sleep(15) ## пауза чтобы ввести капчу

    with allure.step(f"Открыть первую страницу {needed_site} в выдаче поиска с материалом про {needed_title}"):
        google_after_search = GoogleAfterSearch(webdriver)
        google_after_search.check_title_has_needed_link(needed_site)
        google_after_search.open_link_with_site_and_title(needed_site, needed_title)

    with allure.step(f"Проверить в инфо-карточке {needed_title} сведения под заголовком автор"):
        wikipedia_page = WikipediaPage(webdriver)
        wikipedia_page.check_title(needed_title)
        wikipedia_page.check_author(checked_author)

