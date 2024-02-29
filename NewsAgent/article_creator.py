import os 
from dotenv import load_dotenv
from langchain.chains import LLMChain
from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from datetime import date 
from query_constructor import llm_connect
from news_extractor import obtain_articles_from_query

load_dotenv()

# * For each article, generate a bullet point summary of the most impactful facts and quotes (if relevant) mentioned
# * Group per source
def extract_facts_prompt(query, article):
    template: str = """
    Objective: Extract 5-10 relevant, unbiased, and factual bullet points from a news article related to the user's search query: {query}. 
    Include significant quotes if relevant.

    Instructions to deconstruct the article into bullet points: 

    1. Read and Analyze the Article:
        * Skim through the article to get an overall understanding of its content and main message.
        * Identify the who, what, when, where, and why (5Ws) to grasp the essential facts.
    2. Deconstruct the Article:
        * Introduction: Identify the article's main thesis or argument presented in the introduction.
        * Body: Break down the body into sections or themes. For each section, note the key points, supporting evidence, and factual data.
        * Conclusion: Summarize the conclusion or the final thoughts provided by the author, focusing on the resolution or call to action.
    3. Select Relevant Information:
        *Choose information that directly relates to the user's search query. Focus on facts, findings, and data points.
        *Avoid subjective opinions or biased language unless it's a direct quote that adds value to the factual reporting.
    4. Extract Bullet Points:
        * Create bullet points that succinctly summarize the key facts and findings. Each bullet point should stand alone in conveying a complete piece of information.
        * If a direct quote is particularly relevant, include it as one of the bullet points, clearly indicating it's a quote with quotation marks and attributing it to the speaker.
    5. Maintain Unbiased Reporting:
        * Ensure that each bullet point is presented in a neutral tone, avoiding any language that suggests opinion or bias.
        * Focus on reporting what is known and verified, distinguishing between facts and assertions made within the article.
    6. Review and Refine:
        * Review the bullet points to ensure they are clear, factual, and unbiased. Each point should be directly relevant to the user's search query.
        * Refine the language for clarity and conciseness, ensuring that the bullet points are easily understandable.
    
    Remember the objective of extracting from 5 - 10 relevant bullet points using the instructions above. 
    ---

    News article: {article}
"""

    prompt_template = PromptTemplate(
        template=template, input_variables=["query", "article"]
    )

    return prompt_template

def extract_facts_articles(prompt_template, article):
    chain = LLMChain(
        llm = llm_connect(), prompt = extract_facts_prompt(article)
    )

    response = chain.invoke(input={'user_query':user_query, 'today_date':today_date})

def create_stories_prompt(): 
    
    pass

def chain_of_thought(): 
    
    pass

def extract_stories(query):
    articles_dict = obtain_articles_from_query(query)
    print(len(articles_dict))
    for article in articles_dict:
        print(f"ARTICLE: {article['title']}\n=====================\n")
        print(article['text'])


if __name__ == '__main__':
    extract_stories('US Economy this week')