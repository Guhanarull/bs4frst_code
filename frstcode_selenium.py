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
url = "https://stackoverflow.com/questions/17436014/selenium-versus-beautifulsoup-for-web-scraping"

driver.get(url)
try:
    CSS_SELECTOR = "#question-header > h1 > a"
    span_element= (CSS_SELECTOR)

    if span_element:
        print("output is:", span_element.text.strip())
    else:
        print("don't_giveup") 

finally:
    print()