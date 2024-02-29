import os 
import requests

from dotenv import load_dotenv
from query_constructor import generate_search_url

load_dotenv()

def search_articles(query):
    search_url = generate_search_url(query)
    complete_url = search_url + f"&apiKey={os.getenv('NEWSAPI_KEY')}"
    print(complete_url)

    response = requests.get(complete_url)
    if response.status_code == 200: 
        articles_json = response.json()
        for article in articles_json['articles']:
            print(f"Title: {article['title']}")
            print(f"Author: {article['author']}")
            print(f"Published At: {article['publishedAt']}")
            print(f"Source: {article['source']['name']}")
            print(f"URL: {article['url']}\n\n")
        return articles_json['articles']
    else: 
        return None
    
def extract_text_from_articles(articles_dict):
    pass

# * Cuidado con las fechas manito
if __name__ == "__main__":
    query = "Summary of the economy for this week"
    search_articles(query)
