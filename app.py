import requests
from bs4 import BeautifulSoup

# Define the URL of the webpage to scrape
url = 'https://hafizcaniago.my.id'

# Send a GET request to the URL
response = requests.get(url)

# Parse the HTML content of the webpage
soup = BeautifulSoup(response.text, 'html.parser')

# Find elements by their HTML tags
title = soup.h5
print("Title of the webpage:", title.text)

# Find elements by selecting all class
project_titles = soup.find_all('h5')
for project_title in project_titles:
    print(project_title.text)