import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys

driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.maximize_window()
# wait until 5 second if element is not displayed.
# globally to your test
driver.implicitly_wait(5)

driver.get("http://automationpractice.com/")

action = ActionChains(driver)

driver.find_element_by_id("search_query_top").send_keys("dress", Keys.ENTER)
time.sleep(5)
driver.execute_script("window.scrollTo(0, 200)")
driver.find_element_by_xpath("//*[contains(@src,'1/6/16-home')]").click()



# hovering of products
# products = driver.find_elements_by_xpath("//*[@class='product-container']")
# for prod in products:
#     action.move_to_element(prod).perform()
#     time.sleep(5)
#     addToCart = driver.find_element_by_xpath("//*[@title='Add to cart']")
#     driver.execute_script("arguments[0].click();", addToCart)
#     time.sleep(5)
#     continueShopping = driver.find_element_by_xpath("//*[@title='Continue shopping']")
#     driver.execute_script("arguments[0].click();", continueShopping)
