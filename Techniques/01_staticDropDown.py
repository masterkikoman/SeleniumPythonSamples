from selenium import webdriver
from selenium.webdriver.support.select import Select

driver = webdriver.Firefox(executable_path="C:\\Users\\kalmazan\\SeleniumDrivers\\geckodriver.exe")
driver.maximize_window()

driver.get("https://blazedemo.com/")

# StaticDropDown
dropdown = Select(driver.find_element_by_name("fromPort"))
dropdown.select_by_visible_text("San Diego")
dropdown.select_by_index(3)
dropdown.select_by_value("Philadelphia")
title = driver.title
assert "Demo" in title # Substring
assert "BlazeDemo" == title

driver.close()

