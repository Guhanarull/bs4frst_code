import requests
from bs4 import BeautifulSoup

# Specify the URL
url = "https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-github-profile"

# Send an HTTP request to the URL and get the content
response = requests.get(url)
html_content = response.content

# Parse the HTML content with BeautifulSoup
soup = BeautifulSoup(html_content, "html.parser")

try:
    # Use BeautifulSoup to find the desired element using a CSS selector
    css_selector = '#title-h1'
    span_element = soup.select_one(css_selector)

    # Check if the element is found
    if span_element:
        # Print the text content of the found element
        print("Text of the Span:", span_element.text.strip())
    else:
        print("Element not found. Check the CSS selector or the structure of the webpage.")

except Exception as e:
    print("An error occurred:", str(e))
