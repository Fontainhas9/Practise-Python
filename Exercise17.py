import requests
from bs4 import BeautifulSoup

# Make a request to the New York Times homepage
url = "https://www.nytimes.com/"
response = requests.get(url)

# Parse the HTML content of the page using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find all the article titles on the page
article_titles = soup.find_all("h2", class_="css-1qwxefa esl82me0")

# Print out the article titles
for title in article_titles:
    print(title.text)
