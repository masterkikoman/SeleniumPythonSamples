import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.maximize_window()

driver.get("http://automationpractice.com/")
driver.find_element_by_id("search_query_top").send_keys("dress")
time.sleep(3)
# Common locator for every element
dressTypeCount = driver.find_elements_by_xpath("//ul/li[contains(@class,'ac_')]")
len(dressTypeCount)

for dress in dressTypeCount:
    if "Chiffon" in dress.text:
        dress.click()
        break

