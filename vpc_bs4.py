import requests
from bs4 import BeautifulSoup
#import logging
#from datetime import datetime

# Specify the URL of the webpage
url = "https://www.sololearn.com/en/learn/courses/python-introduction/lesson/2169371533?p=4"

# Set up logging
log = "guhan.txt"
#logging.basicConfig(filename=log, level=logging.INFO, format="%(asctime)s - %(levelname)s: %(message)s")

# Log initiation time and URL
#logging.info("Script initiated on %s for URL: %s", datetime.now().strftime("%Y-%m-%d %H:%M:%S"), url)

# Send an HTTP request to the URL and get the content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Use the provided identifier to find the desired element
identifier = "Memory & Variables"
result = soup.find("h1", {"id": identifier})

# Check if the element is found
if result:
    # Print the text content of the found element
    scraped_data = result.text.strip()
    print("Scraped Data:", scraped_data)

    # Log the scraped data
    #logging.info("Scraped Data: %s", scraped_data)
else:
    print("Element not found. Check the identifier or the structure of the webpage.")
    #logging.warning("Element not found for identifier: %s", identifier)

# Close the logging file
#logging.shutdown()
