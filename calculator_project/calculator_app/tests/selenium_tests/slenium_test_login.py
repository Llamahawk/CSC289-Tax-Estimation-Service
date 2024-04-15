from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.chrome.service import Service
import time

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

# Open the webpage
driver.get("http://127.0.0.1:8000/calculator_app/ ")

# Wait for the page to load
time.sleep(3)

# Click the "Sign Up" button
sign_up_button = driver.find_element(By.ID, "login")
sign_up_button.click()

# Wait for the sign-up page to load
time.sleep(3)

# Fill in the email
email_input = driver.find_element(By.ID,"email_address")
email_input.send_keys("aj5678@example.com")

# Fill in the password
password_input = driver.find_element(By.ID,"password")
password_input.send_keys("Password#1567")

time.sleep(5)

# Find and click the submit button
submit_button = driver.find_element(By.XPATH, "//input[@type='submit']")
submit_button.click()

# Wait for the sign-up process to complete
time.sleep(4)

income_input = driver.find_element(By.ID, "income")
income_input.send_keys(1200)

status_dropdown = Select(driver.find_element(By.ID, "filing_status"))
status_dropdown.select_by_value("5")

time.sleep(4)

cal_button = driver.find_element(By.XPATH, "//input[@type='submit']")
cal_button.click()

time.sleep(10)
# Quit the WebDriver
driver.quit()
