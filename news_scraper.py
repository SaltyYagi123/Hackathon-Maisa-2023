import requests
import newspaper
from newspaper import Article
from bs4 import BeautifulSoup

news_regions = ['world','africa','asia','australia','europe','latin america','middle east', 'US & Canada']
# * Careful because these aren't articles, they are portals
news_sources_world = {'bbc': 'https://www.bbc.com/news/world', 'time':'https://time.com/section/world', 'france24':'https://www.france24.com/en/world', 'apnews':'https://apnews.com/world-news', 'the_independent':'https://www.independent.co.uk/world', 'euronews':'https://www.euronews.com/news/international', 'cnn_espana':'https://cnnespanol.cnn.com/seccion/mundo/',}
news_sources_spain = {'larazon':'https://www.larazon.es/', 'hkfp':'https://hongkongfp.com/'}

# TODO - Access to the serpApi for Google News - Regional based

def fetch_article_links(news_sources_dict): 
    all_links = {}
    for source, url in news_sources_dict.items():
        try:
            response = requests.get(url)
            soup = BeautifulSoup(response.content, 'html.parser')
         
            # Normalize and complete relative links if necessary
            links = [a['href'] for a in soup.find_all('a', href=True)]
            # Store in dictionary
            all_links[source] = links
        except Exception as e:
            print(f"An error occurred while fetching links from {url}: {e}")
            all_links[source] = []  # Store an empty list in case of an error

    return all_links


article_links_dict = fetch_article_links(news_sources_world)

for source, links in article_links_dict.items():
    print(f"News Source: {source}\n========\n\n")
    for link in links:
        print(link)

# * Each source has its own format, but approximately the same 