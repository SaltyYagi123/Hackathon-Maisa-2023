import os
from dotenv import load_dotenv
from langchain import hub 
from langchain.agents import (
    create_react_agent, 
    AgentExecutor
)
from langchain_core.prompts import PromptTemplate
from langchain_openai import ChatOpenAI

load_dotenv()

def url_constructor(user_query:str) -> str: 
    llm = ChatOpenAI(temperature= 0.3, model_name='gpt-3.5-turbo')
    template = """Your job is to construct a URL for an API given the search query: '{user_query}' 
    Consider the following factors: 
     - The language in which the query is written.
     - Identify key words or phrases from the query, to extract the search topic. Consider if we need to search for a top relevant story or a general search. 
     - The time period that the user might be interested in searching by writing that query.
     - If there is a specified domain name included, to search for specific publishers. 

    Once you've considered and specified each factor in list form, construct a URL to call the NewsAPI using the following schema. Your task is to fill in the content between {}: 
    1. If the query is generalistic, generate it in the following format: 
        https://newsapi.org/v2/everything?q={keywords-or-phrases}&from={YYYY-MM-DD}&to={YYYY-MM-DD}&sortBy=popularity&language={2-letter ISO-639-1 code of the language}&pageSize=10
    2. If the query is for a trending topic, generate it in the following format: 
        https://newsapi.org/v2/top-headlines?q={keywords-or-phrases}&country={2-letter ISO 3155-1 code for the country}&category={business|entertainment|general|health|science|sports|technology}&pageSize=10
    
    Example queries:    
    * Generalistic: 
        Articles about Bitcoin - https://newsapi.org/v2/everything?q=bitcoin
        Articles mentioning Apple yesterday, sorted by popular publishers first - https://newsapi.org/v2/everything?q=apple&from=2024-02-28&to=2024-02-28&sortBy=popularity
        Articles published by TechCrunch and TheNextWeb - https://newsapi.org/v2/everything?domains=techcrunch.com,thenextweb.com&apiKey=API_KEY

    * Trending:
        Top headlines in the US - https://newsapi.org/v2/top-headlines?country=us
        Top headlines from BBC News - https://newsapi.org/v2/top-headlines?sources=bbc-news
        Top headlines about Trump - https://newsapi.org/v2/top-headlines?q=trump

    Your answer should be only the URL constructed based on the user search query, following the rules specified above."""

    prompt_template = PromptTemplate(
        template = template, input_variables=["user_query"]
    )
    formatted_prompt = prompt_template.format(user_query=user_query)
    response = llm.invoke(formatted_prompt)
    return response