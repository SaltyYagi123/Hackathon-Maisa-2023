import os 
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from agents.url_constructor_agent import url_constructor

load_dotenv()

def llm_connect(): 
    llm = ChatOpenAI(
        temperature= 0, model_name='gpt-4', api_key=os.getenv("OPENAI_API_KEY")
    )
    return llm 

def generate_url(query):
    template: str = """
    Your task is to generate a URL for NewsAPI that directly corresponds to {user_query}. 
    Focus on identifying the most relevant keywords or phrases from the query "{user_query}" to ensure the URL will fetch articles closely related to the topic.

    Key considerations for constructing the URL:
    - Extract the main topic or keywords from "{user_query}" accurately.
    - Determine the appropriate time frame for the search, if applicable.
    - Use the correct language setting based on the query's language.
    - For general searches, format the URL as follows:
    https://newsapi.org/v2/everything?q={{main-topic-or-keyword}}&from={{start-date}}&to={{end-date}}&sortBy=popularity&language={{language-code}}&pageSize=10
    - For trending or specific topic searches, use this format:
    https://newsapi.org/v2/top-headlines?q={{main-topic-or-keyword}}&country={{country-code}}&category={{category}}&pageSize=10

    Remember, the placeholders within {{}} should be replaced with information relevant to the search query. Aim for precision in keyword selection to ensure the resulting articles are on-topic.

    Example task:
    Given the search query "NVIDIA Stock Jump", construct a URL that fetches the most recent and relevant articles about this topic from NewsAPI.

    Focus on accuracy and relevancy in your response. Remember, only return the URL generated, don't give any further explanation.
"""
# Correctly use the named placeholder in the format call
    prompt_template = PromptTemplate(template = template, input_variables=['user_query'])

    return prompt_template

if __name__ == "__main__":
    user_query = ""
    # Creating an LLMChain instance
    chain = LLMChain(llm=llm_connect(), prompt=generate_url(user_query))
    # Run the chain to get the response
    response = chain.invoke(input={"user_query": user_query})
    print(response)
