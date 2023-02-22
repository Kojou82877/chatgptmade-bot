from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# set up the web driver
options = webdriver.ChromeOptions()
options.add_argument("start-maximized")
driver = webdriver.Chrome(options=options)

# log in to Facebook
driver.get("https://www.facebook.com/")
email_input = driver.find_element_by_name("email")
password_input = driver.find_element_by_name("pass")
email_input.send_keys("your-email@example.com")
password_input.send_keys("your-password")
password_input.send_keys(Keys.ENTER)

# wait for login to complete
time.sleep(5)

# navigate to chat/inbox
driver.get("https://www.facebook.com/messages/t/123456789") # replace with chat/inbox link
time.sleep(5)

# read messages from notepad file and send them
with open("message_file.txt", "r") as f:
    messages = f.readlines()
for message in messages:
    message_input = driver.find_element_by_css_selector("div[data-pagelet='ChatTab']")
    message_input.click()
    message_input.send_keys(message)
    message_input.send_keys(Keys.ENTER)
    time.sleep(5)

# close the web driver
driver.quit()
