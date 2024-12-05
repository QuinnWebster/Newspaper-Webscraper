import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
import re
import time
from sumy.parsers.plaintext import PlaintextParser
from sumy.nlp.tokenizers import Tokenizer
from sumy.summarizers.lsa import LsaSummarizer


#This gets top 5 articles from rocky mountain outlook and summarizes them

def generate_summary(text, sentences_count=10):
    # Create a plaintext parser
    parser = PlaintextParser.from_string(text, Tokenizer("english"))

    # Create an LSA summarizer
    summarizer = LsaSummarizer()

    # Summarize the text
    summary = summarizer(parser.document, sentences_count)

    # Print the summary
    for sentence in summary:
        print(sentence)



def get_status_code(newsurl, headers):

    # Send an HTTP GET request to the URL with headers
    return requests.get(newsurl, headers=headers)


def parse_text(response):
        return BeautifulSoup(response.text, 'html.parser')

def get_list_of_titles(soup):
     
    return soup.find_all('a', {'aria-label': True})



def get_list_of_article_links(soup):
     

        list_of_articles = [a['href'] for a in soup.find_all('a', class_='article-card__link')]


        base_url = 'https://www.thecragandcanyon.ca/'

        list_of_article_links = [base_url + link for link in list_of_articles]

        return list_of_article_links




def get_summary():

    #Newspaper URL
    newsurl = "https://www.thecragandcanyon.ca/category/news/local-news/"

    #Makes it look like a web browser
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.3"
    }
    
    response = get_status_code(newsurl, headers)

    if response.status_code == 200:

        soup = parse_text(response)

        list_of_titles = get_list_of_titles(soup)

        list_of_article_links = get_list_of_article_links(soup)

    
    for i, article in enumerate(list_of_article_links):
        if i >= 1:
             break

        response2 = requests.get(article, headers=headers)
    
        if response2.status_code == 200:

            #Represents the parsed HTML
            soup2 = BeautifulSoup(response2.text, 'html.parser')

            paragraph_tags = soup2.find_all('p')

            full_article_text = ''

            unwanted_words = ['Crag & Canyon', 'about cookies here', 'Terms and Services >', 'Community Guidelines for more', 'Toronto, Ontario, M']

            for paragraph in paragraph_tags:
        
                has_unwanted_words = any(unwanted_word in paragraph.text for unwanted_word in unwanted_words)

                if not has_unwanted_words:

                    full_article_text = full_article_text + ' ' + paragraph.text 

            #print(full_article_text)

            generate_summary(full_article_text)
            print()
            print()



   
if __name__ == "__main__":
    get_summary()
