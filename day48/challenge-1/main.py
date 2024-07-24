from selenium import webdriver
from selenium.webdriver.common.by import By

# Keep chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)


# Create and configure a chrome driver
driver = webdriver.Chrome(options=chrome_options)

driver.get("https://www.python.org")
event_times = driver.find_elements(By.CSS_SELECTOR, value=".event-widget time")
event_names = driver.find_elements(By.CSS_SELECTOR, value=".event-widget ul a")

events = {}

for n in range(len(event_times)):
    events[n] = {
        "time": event_times[n].text,
        "event": event_names[n].text
    }

print(events)

driver.close()
