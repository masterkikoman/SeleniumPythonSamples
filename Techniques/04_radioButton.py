import time

from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.maximize_window()

driver.get("https://www.philippineairlines.com/en/ph/home")
radioButton = driver.find_elements_by_xpath("//div[@class='flight_type_container']/div[contains(@class,'radio-btn')]")
print(len(radioButton))
for radioValue in radioButton:
    if radioValue.text == "One Way":
        radioValue.click()
        time.sleep(3)
        break

assert "One Way" in radioValue.text

