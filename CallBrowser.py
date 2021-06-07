from selenium import webdriver
# every browser exposes an executable file
# Need to invoke executable file through selenium test
# which will then invoke actual browser

driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.maximize_window()

driver.get("http://automationpractice.com/")

# getting the title of the webpage
print(driver.title)
# getting the current url
print(driver.current_url)

driver.get("https://www.udemy.com/")
driver.back()
driver.refresh()
driver.close()
