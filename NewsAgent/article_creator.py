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
        Objective: Extract relevant, unbiased, and factual bullet points from a news article related to the user's search query: {query}. 
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
        
        Remember the objective of extracting relevant bullet points using the instructions above.
        Be sure to only reply with the extracted bullet points and quotes.
        ---
        News article to analyse: {article}
    """

    prompt_template = PromptTemplate(
        template=template, input_variables=["query", "article"]
    )

    return prompt_template

def extract_facts_articles(user_query, article):
    chain = LLMChain(
        llm = llm_connect(), prompt = extract_facts_prompt(user_query, article)
    )
    response = chain.invoke(input={'user_query':user_query, 'article':article})
    return response['text']

def articles_bullet_point_dictionary(user_query, articles_dict):
    bullet_point_articles = {}
    for article in articles_dict: 
        source_name = article['source']
        source_url = article['url']
        bullet_points = extract_facts_articles(article['text'], user_query)
        print(bullet_points)

        if source_name not in bullet_point_articles: 
            bullet_point_articles[source_name] = {
                'source_url': source_url, 
                'articles': []
            }
        
        bullet_point_articles[source_name]['articles'].append({
            'title': article['title'], 
            'bullet_points': bullet_points
        })
    return bullet_point_articles

def create_stories_prompt(): 
    
    pass

def chain_of_thought(): 
    
    pass

if __name__ == '__main__':
    query = 'US Economy this week'
    articles_dict = obtain_articles_from_query(query)
    print(articles_dict)
    articles_bullet_point_dictionary(articles_dict, query)

#TODO - LOGO + UI + END-END DEMO + PRESENTACIÓN + PROMPTS + (+1,-1)
#TODO - ElevenLabs
#TODO - PRESENTACIÓN: 
# * Questions Part:
# *     How you could potentially monetise what we’re doing 
# *     B2C Positioning? 
# *     Ads? 
# *     Monetise the podcast -> Free to interact to the agent, by inserting some ads, within the actual loop. 
# *     Channel 1 - NewsAI - You are the driving force for this - Personalised global news network. 
# *     Policy + News - Social Impact 
# * ——
# *     What’s the problem (Stats, the problem, the problem, the problem) -> Future-proofing the news. 
# *     The architecture of the problem -> Maisa 
# *     More technical oriented -> Tell them the story and the vision. 
# *     Don’t mention monetisation 