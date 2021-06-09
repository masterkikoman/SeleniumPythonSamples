import time

from selenium import webdriver
driver = webdriver.Firefox(executable_path="C:\\Users\\kalmazan\\SeleniumDrivers\\geckodriver.exe")
driver.maximize_window()

driver.get("https://www.w3schools.com/tags/tryit.asp?filename=tryhtml5_input_type_checkbox")
time.sleep(3)
iframe = driver.find_element_by_id("iframeResult")
driver.switch_to.frame(iframe)
checkbox = driver.find_elements_by_xpath("//*[@type='checkbox']")

for check in checkbox:
    check.click()
    assert check.is_selected() #check if all checkbox are selected

driver.find_element_by_xpath("//*[@type='submit']").click()
message = driver.find_element_by_xpath("//body/h2").text
assert "received" in message

driver.switch_to.default_content()
driver.close()

