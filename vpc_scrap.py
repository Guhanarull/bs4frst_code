import logging
import sys
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService

# Set the path to the ChromeDriver executable
chrome_path = r"C:\Program Files\Google\Chrome\Application\chromedriver.exe"

# Set up logging
logging.basicConfig(filename="selenium_script.log", level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

# Create a file for output and error
output_file = open("output.txt", "w")
error_file = open("error.txt", "w")

# Redirect standard output and standard error to files
sys.stdout = output_file
sys.stderr = error_file

# Create a Chrome driver instance using Service
chrome_service = ChromeService(chrome_path)
driver = webdriver.Chrome(service=chrome_service)

try:
    # Navigate to the specified URL
    url = "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html"
    driver.get(url)

    # Find the element using the provided XPath
    xpath = '//*[@id="what-is-amazon-vpc"]'
    element = driver.find_element("xpath", xpath)

    # Extract and log the text content of the element
    logging.info("Scraped Data: %s", element.text)

except Exception as e:
    # Log any exceptions
    logging.error("An error occurred: %s", str(e))

finally:
    # Close the browser window
    driver.quit()

    # Close the output and error files
    output_file.close()
    error_file.close()

    # Restore standard output and standard error
    sys.stdout = sys.__stdout__
    sys.stderr = sys.__stderr__
