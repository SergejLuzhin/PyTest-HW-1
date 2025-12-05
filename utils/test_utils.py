import allure
from allure_commons.types import AttachmentType

from conftest import chromedriver

def allure_screenshot(chromedriver, name):
    """Делает скриншот текущей страницы и прикрепляет его к Allure-отчёту.

        Назначение:
            Получает скриншот из браузера через WebDriver и добавляет его как вложение
            в Allure-отчёт с указанным именем.

        Параметры:
            webdriver: Экземпляр Selenium WebDriver, из которого берётся скриншот.
            name (str): Имя вложения, под которым скриншот будет отображаться в Allure.

        Автор: Сергей Лужин
        """
    allure.attach(chromedriver.get_screenshot_as_png(),
                  name=name, attachment_type=AttachmentType.PNG)
