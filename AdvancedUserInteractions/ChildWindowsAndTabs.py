from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Drivers\\geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/windows")
driver.find_element_by_link_text("Click Here").click()

# add the childId of your window
# driver.window_handles method which will get all the windows open by automation
childWindow = driver.window_handles[1]
# ("parentid", "childid")
driver.switch_to.window(childWindow)
text = driver.find_element_by_tag_name("h3").text
print(text)
assert "New Window" == text
parentdWindow = driver.window_handles[0]
driver.switch_to.window(parentdWindow)
text = driver.find_element_by_tag_name("h3").text
print(text)
assert "Opening a new window" == text
driver.close()