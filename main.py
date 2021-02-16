from selenium import webdriver

chrome_browser = webdriver.Chrome('./chromedriver')
chrome_browser.get('https://www.seleniumeasy.com/test/basic-first-form-demo.html')

assert 'Selenium Easy Demo' in chrome_browser.title
show_msg_button = chrome_browser.find_element_by_class_name('btn-default')

assert 'Show Message' in chrome_browser.page_source

user_message = chrome_browser.find_element_by_id('user-message')
user_message.clear()
user_message.send_keys('heyyaaaa')
show_msg_button.click()
