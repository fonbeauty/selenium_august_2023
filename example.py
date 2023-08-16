from selenium import webdriver
from selenium.webdriver.chrome.service import Service

service = Service(executable_path="C:\\Users\\bilbo\\tools\\drivers\\chromedriver.exe")
chrome = webdriver.Chrome(service=service)
pass
