import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
driver = webdriver.Firefox(executable_path="C:\\Users\\kalmazan\\SeleniumDrivers\\geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(15)

driver.get("http://automationpractice.com/")

action = ActionChains(driver)
driver.find_element_by_id("search_query_top").send_keys("dress", Keys.ENTER)
time.sleep(5)
driver.execute_script("window.scrollTo(0, 200)")

# hovering of products
products = driver.find_element_by_xpath("//*[contains(@src,'1/6/16-home')]")
action.move_to_element(products).perform()
time.sleep(5)
addToCart = driver.find_element_by_xpath("//*[@title='Add to cart']")
driver.execute_script("arguments[0].click();", addToCart)
