#This prints the top article from the craig and canyon

import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re

#Newspaper URL
newsurl = "https://www.rmoutlook.com/local-news/"

#Makes it look like a web browser
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3"
}

# Send an HTTP GET request to the URL with headers
response = requests.get(newsurl, headers=headers)

#If the request was successfull the code should be 200
if response.status_code == 200:

    #Soup repersents the parsed HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    target_h2 = soup.find('h2', class_='media-heading mt-0 mb-1')

    if target_h2:
        extracted_text = target_h2.get_text(strip=True)
        print("Extracted text:")
        print(extracted_text)

        article_link = soup.find('a', class_='media media-bordered')['href']

    else:
        print("The h2 element was not found.")

    print("Link:")
    full_url = "https://www.rmoutlook.com/" + article_link

    print(full_url)

    secondURL = full_url

    response2 = requests.get(secondURL, headers=headers)

    if response2.status_code == 200:

        #Represents the parsed HTML
        soup2 = BeautifulSoup(response2.text, 'html.parser')


        paragraph_tags = soup2.find_all('p')

        full_article_text = ''

        unwanted_words = ['Vote', 'Results >', 'Archives >', '© 2024 Rocky Mountain Outlook', ' Sign In Register CANMORE']

        for paragraph in paragraph_tags:
    
            has_unwanted_words = any(unwanted_word in paragraph.text for unwanted_word in unwanted_words)


            if not has_unwanted_words:

                #print(paragraph.text)

                full_article_text = full_article_text + ' ' + paragraph.text 

        print(full_article_text)


