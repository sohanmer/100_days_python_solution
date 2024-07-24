from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Create and configure a chrome driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://secure-retreat-92358.herokuapp.com/")

first_name = driver.find_element(By.CSS_SELECTOR, "[name='fName']")
first_name.send_keys("FirstName")

last_name = driver.find_element(By.CSS_SELECTOR, "[name='lName']")
last_name.send_keys("LastName")

email = driver.find_element(By.CSS_SELECTOR, "[name='email']")
email.send_keys("test@gmail.com")

submit = driver.find_element(By.CSS_SELECTOR, "[type='submit']")
submit.click()

driver.close()
