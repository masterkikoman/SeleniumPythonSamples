import time

from selenium import webdriver
from selenium.webdriver import ActionChains

# driver = webdriver.Firefox(executable_path="C:\\Users\\kalmazan\\SeleniumDrivers\\geckodriver.exe")
driver = webdriver.Chrome("C:\\Users\\kalmazan\\SeleniumDrivers\\Chromedriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)
action = ActionChains(driver)


driver.get("https://chercher.tech/practice/practice-pop-ups-selenium-webdriver")
doubleClick = driver.find_element_by_id("double-click")
action.context_click(doubleClick).perform()
action.double_click(doubleClick).perform()

alert = driver.switch_to.alert

assert "double clicked" in alert.text
alert.accept()
driver.close()
