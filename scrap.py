import os
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException

# Get environment variables
chrome_path = 'C:\Program Files\Google\Chrome\Application'

service = Service(chrome_path + "/chromedriver.exe")
options = webdriver.ChromeOptions()
options.binary_location = chrome_path + "/chrome.exe"

url ="https://www.cabelas.com/shop/en/garmin-epix-pro-gen-2-standard-edition-smartwatch"
chrome_options = options()
chrome_options.add_argument("--headless")  # Run Chrome in headless mode
chrome_options.add_argument("--user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")

# Initialize the Chrome driver
driver = webdriver.Chrome(options=chrome_options)

# Navigate to the URL
driver.get(url)

# Wait for the price element to be present
try:
    price_element = WebDriver(driver, 10).until(
        ElementClickInterceptedException.presence_of_element_located((By.CLASS_NAME, "price"))
    )

    # Extract the price text
    price = price_element.text.strip()
    print(f"The price is: {price}")
except Exception as e:
    print(f"Error: {e}")
finally:
    # Close the browser window
    driver.quit()
