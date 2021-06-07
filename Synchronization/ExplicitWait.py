# Wait to target specific element
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.maximize_window()

driver.get("http://automationpractice.com/")
wait = WebDriverWait(driver, 15)
action = ActionChains(driver)

driver.find_element_by_id("search_query_top").send_keys("dress", Keys.ENTER)
time.sleep(5)
driver.execute_script("window.scrollTo(0, 200)")
driver.find_element_by_xpath("//*[contains(@src,'1/6/16-home')]").click()
wait.until(EC.frame_to_be_available_and_switch_to_it((By.XPATH, "//*[@class='fancybox-iframe']")))
addToCart = wait.until(EC.element_to_be_clickable((By.XPATH, "//*[@name='Submit']")))
# addToCart = driver.find_element_by_xpath("//*[@name='Submit']")
# ele = wait.until(EC.presence_of_element_located((By.XPATH, addToCart)))
driver.execute_script("arguments[0].click();", addToCart)
driver.switch_to.default_content()
message = driver.find_element_by_xpath("//div[contains(@class,'layer_cart_product')]/h2")
message.is_displayed()
