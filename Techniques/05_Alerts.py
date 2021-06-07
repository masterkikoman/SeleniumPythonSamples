from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.maximize_window()
driver.get("https://www.w3schools.com/js/tryit.asp?filename=tryjs_alert")

iframe = driver.find_element_by_id("iframeResult")
driver.switch_to.frame(iframe)
driver.find_element_by_xpath("//button[@onclick='myFunction()']").click()
alert = driver.switch_to.alert
print(alert.text)
assert "alert" in alert.text
alert.accept() # click on ok in alert button

# if alerts has OK or Cancel in Choices
# use alert.dismiss()

