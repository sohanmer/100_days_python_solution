from selenium import webdriver
from selenium.webdriver.common.by import By
import time


chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.linkedin.com/login/")

user_name = "username"
passwd = "password"

username = driver.find_element(by=By.ID, value="username")
username.send_keys(user_name)

password = driver.find_element(by=By.ID, value="password")
password.send_keys(passwd)

submit_button = driver.find_element(by=By.CSS_SELECTOR, value="[data-litms-control-urn='login-submit']")
submit_button.click()

jobs_button = driver.find_element(by=By.CSS_SELECTOR, value="[title='Jobs']")
jobs_button.click()

time.sleep(5)
jobs = driver.find_elements(by=By.CSS_SELECTOR, value=".job-card-container--clickable")

for job in jobs:
    job.click()
    time.sleep(5)
    save_button = driver.find_element(by=By.CSS_SELECTOR, value=".jobs-save-button")
    save_button.click()
