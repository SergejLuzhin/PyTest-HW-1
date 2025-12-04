import allure
from allure_commons.types import AttachmentType

from conftest import chromedriver

def allure_screenshot(chromedriver, name):
    allure.attach(chromedriver.get_screenshot_as_png(),
                  name=name, attachment_type=AttachmentType.PNG)
