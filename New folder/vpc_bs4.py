import requests
from bs4 import BeautifulSoup

# Specify the URL of the webpage
url = "https://docs.aws.amazon.com/vpc/latest/userguide/what-is-amazon-vpc.html"

# Send an HTTP request to the URL and get the content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

# Find all text within <div> tags on the webpage
div_texts = [div.text.strip() for div in soup.find_all("div")]

# Print the scraped data
print("Scraped Data:")
for text in div_texts:
    print(text)
