from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service as ChromeService
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Set the path to the ChromeDriver executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# Create a Chrome driver instance using Service
chrome_service = ChromeService(chrome_path)
driver = webdriver.Chrome(service=chrome_service)

# Specify the URL
url = "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile"

# Navigate to the specified URL
driver.get(url)

try:
    # Use an implicit wait to wait for the element to become available
    driver.implicitly_wait(10)  # Adjust the timeout if needed

    # Use Selenium to find the desired element using a CSS selector
    css_selector = '#title-h1'
    span_element = driver.find_element(By.CSS_SELECTOR, css_selector)

    # Print the text content of the found element
    print("Text of the Span:", span_element.text.strip())

except Exception as e:
    print("An error occurred:", str(e))

finally:
    # Close the browser window
    driver.quit()
