from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By


def test_two(driver: WebDriver):
    driver.get("https://demowebshop.tricentis.com/")
    assert driver.title.title() == 'Demo Web Shop'


def test_three(driver: WebDriver):
    driver.get("https://demowebshop.tricentis.com/")
    assert driver.title.title() == 'DemoWebShop'

def test_four(driver: WebDriver):
    driver.get("https://demowebshop.tricentis.com/")
    driver.find_element(By.CSS_SELECTOR, 'a[href="/books"]').click()
    assert driver.find_element(By.TAG_NAME, 'h1').text == 'Books'
    pass

