import os 
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate

load_dotenv()

def llm_connect(): 
    llm = ChatOpenAI(
        temperature= 0.3, model_name='gpt-3.5-turbo', api_key=os.getenv("OPENAI_API_KEY")
    )
    return llm 

def generate_url(): 
    url_generation_prompt = """
    Given the search request: {search_query}, consider all of the following factors: 
     - The language in which the query is written.
     - Keywords or phrases from the query, as to extract the search topic.
     - The time period that the user might be interested in searching for having written that query.
     - If there is a specified domain name, to search for specific publishers. 

    Once you've considered and specified each factor in list form, generate a URL so I can query NewsAPI correctly. 
"""
    url_generation_template = PromptTemplate(
        input_variables=['search_query'], template = url_generation_prompt
    )
    return url_generation_template

if __name__ == "__main__":
    chain = LLMChain(llm = llm_connect(), prompt = generate_url())
    user_query = user_query_agent(query="NVIDIA Stock Jump")
    print(user_query)