import requests
from bs4 import BeautifulSoup

# URL of the page to scrape
url = "https://ci.richmond.ca.us/186/Forms-and-Resources"

# Request the page
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    page_content = response.content
    soup = BeautifulSoup(page_content, 'html.parser')

    # Find all links (or specific elements) to the files
    file_links = soup.find_all('a', href=True)
    print(file_links)

    for link in file_links:
        file_url = link['href']
        print(link)
        # print(file_url)
        if "pdf" in file_url:  # Adjust the condition based on the file type
            print(file_url)

else:
    print("Failed to retrieve the webpage")
