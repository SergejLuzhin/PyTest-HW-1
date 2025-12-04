# pylint: disable=no-member
# pylint: disable=missing-function-docstring
# pylint: disable=missing-module-docstring

import allure
import pytest
from selenium import webdriver

@allure.title("Подготовка драйвера")
@pytest.fixture(scope="package")
def chromedriver():
    """
    Фикстура для инициализации и закрытия браузера.
    """
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)
    driver.maximize_window()
    yield driver
    driver.quit()