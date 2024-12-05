
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

    list_of_target_h2 = soup.find_all('h2', class_='media-heading mt-0 mb-1')

    list_of_article_links = [a['href'] for a in soup.find_all('a', class_='media media-bordered')]

    base_url = 'https://www.rmoutlook.com/'


    list_of_article_links = [base_url + link for link in list_of_article_links]

    
    for article in list_of_article_links:

        response2 = requests.get(article, headers=headers)
    
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


