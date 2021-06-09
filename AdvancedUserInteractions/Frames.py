from selenium import webdriver

driver = webdriver.Firefox(executable_path="C:\\Users\\kalmazan\\SeleniumDrivers\\geckodriver.exe")
driver.maximize_window()
driver.implicitly_wait(10)

driver.get("https://the-internet.herokuapp.com/frames")
driver.find_element_by_link_text("iFrame").click()
iframe = driver.find_element_by_id("mce_0_ifr")
driver.switch_to.frame(iframe)
driver.find_element_by_css_selector("#tinymce").clear()
driver.find_element_by_css_selector("#tinymce").send_keys("I am on the iframe")
driver.switch_to.default_content()
print(driver.find_element_by_tag_name("h3").text)