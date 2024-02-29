import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.webdriver import WebDriver


@pytest.fixture(scope='function')
def driver() -> WebDriver:
    service = Service(executable_path="C:\\Users\\bilbo\\tools\\drivers\\chromedriver.exe")
    chrome = webdriver.Chrome(service=service)

    yield chrome

    chrome.quit()
