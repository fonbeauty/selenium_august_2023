import pytest
from selenium import webdriver


@pytest.fixture(scope='function')
def browser():
    driver = webdriver.Chrome()
    driver.get("https://www.selenium.dev/selenium/web/web-form.html")

    yield driver

    driver.quit()

@pytest.fixture(scope='function')
def driver():
    driver = webdriver.Chrome()

    yield driver

    driver.quit()
