import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def test_example():
    service = Service(executable_path="C:\\Users\\bilbo\\tools\\drivers\\chromedriver.exe")
    chrome = webdriver.Chrome(service=service)
    chrome.get(url='https://google.com')
    chrome.get("https://demowebshop.tricentis.com/")
    assert chrome.title.title() == 'Demo Web Shop'
    time.sleep(1)
    pass

def test_example_2():
    service = Service(executable_path="C:\\Users\\bilbo\\tools\\drivers\\chromedriver.exe")
    chrome = webdriver.Chrome(service=service)
    chrome.get(url='https://google.com')
    chrome.get("https://demowebshop.tricentis.com/")
    assert chrome.title.title() == 'Demo Web Shop'
    time.sleep(1)
    pass

def test_example_3():
    service = Service(executable_path="C:\\Users\\bilbo\\tools\\drivers\\chromedriver.exe")
    chrome = webdriver.Chrome(service=service)
    chrome.get(url='https://google.com')
    chrome.get("https://demowebshop.tricentis.com/")
    assert chrome.title.title() == 'Demo Web Shop'
    time.sleep(1)
    pass


def test_example_4():
    service = Service(executable_path="C:\\Users\\bilbo\\tools\\drivers\\chromedriver.exe")
    chrome = webdriver.Chrome(service=service)
    chrome.get(url='https://google.com')
    chrome.get("https://demowebshop.tricentis.com/")
    assert chrome.title.title() == 'Demo Web Shop'
    time.sleep(1)
    pass

