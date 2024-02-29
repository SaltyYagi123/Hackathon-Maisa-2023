import os 
import requests
import newspaper 
import pandas as pd
import concurrent.futures

from newspaper import Article
from dotenv import load_dotenv
from query_constructor import generate_search_url
from newspaper import news_pool

load_dotenv()

def get_articles(query):
    # TODO - Uncomment for real demo, right now, we want to save on API usage
    #search_url = generate_search_url(query)
    #complete_url = search_url + f"&apiKey={os.getenv('NEWSAPI_KEY')}"
    complete_url = 'https://newsapi.org/v2/everything?q=US economy&from=2024-02-23&to=2024-02-29&sortBy=popularity&language=en&pageSize=10&apiKey=6ddc83d9e2974d0fabbac57924805fa3'
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

def extract_article_data(url):
    try: 
        article = Article(url)
        article.download()
        article.parse()
        article.nlp()
        return {
            'text': article.text, 
            'top_image': article.top_image
        }
    except Exception as e: 
        print(f"Error processing {url}: {e}")
        return None

def process_articles_concurrently(articles_dict):
    with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
        # Create a future for each article URL
        future_to_article = {executor.submit(extract_article_data, article['url']): article for article in articles_dict}
        
        for future in concurrent.futures.as_completed(future_to_article):
            article = future_to_article[future]
            try:
                data = future.result()
                if data:
                    # Update the original article dictionary with the extracted text and image
                    article['text'] = data['text']
                    article['top_image'] = data['top_image']
                    print(f"Processed article: {article['title'][:50]} - Image: {article['top_image']}")
            except Exception as exc:
                print(f"Article at {article['url']} generated an exception: {exc}")


# * Cuidado con las fechas manito
if __name__ == "__main__":
    query = "State of the US economy for this week"
    articles_dict = get_articles(query)
    process_articles_concurrently(articles_dict)
    print(articles_dict)
