from selenium.webdriver.common.by import By




def test_first(browser):
    title = browser.title
    browser.implicitly_wait(0.5)
    text_box = browser.find_element(by=By.CSS_SELECTOR, value='[name="my-text"]')
    text_box2 = browser.find_elements(by=By.CSS_SELECTOR, value='[name="my-text"]')
    submit_button = browser.find_element(by=By.CSS_SELECTOR, value="button")
    text_box.send_keys("Selenium")
    submit_button.click()
    message = browser.find_element(by=By.ID, value="message")
    assert message.text == "Received!"
