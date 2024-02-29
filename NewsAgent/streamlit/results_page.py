import streamlit as st
from article_creator import create_article  # Ensure these imports work based on your project structure
from news_extractor import obtain_articles_from_query

def display_results_page():
    if 'user_query' in st.session_state:
        user_query = st.session_state.user_query

        col1, col2 = st.columns([7, 3])

        with col1:
            placeholder = st.empty()  # Placeholder for LLM response
            placeholder.markdown("Loading LLM response...")

            @st.experimental_singleton
            def fetch_llm_response(query):
                # Simulated delay for LLM response (replace with actual logic)
                import time
                time.sleep(2)  # Simulate delay for demonstration
                return create_article(query)

            llm_response = fetch_llm_response(user_query)
            placeholder.markdown(llm_response)

        with col2:
            articles = obtain_articles_from_query(user_query)

            for i in range(0, len(articles), 2):  # Process articles in pairs
                row = st.container()  # Container for each row
                with row:
                    col1, col2 = st.columns(2)  # Two columns per row
                    
                    if i < len(articles):
                        article = articles[i]
                        with col1:
                            st.image(article['image'], width=100)
                            st.write(article['title'])
                            st.button("Visit Source", key=f"btn{i}")
                            st.write(article['summary'])

                    if i + 1 < len(articles):
                        article = articles[i + 1]
                        with col2:
                            st.image(article['image'], width=100)
                            st.write(article['title'])
                            st.button("Visit Source", key=f"btn{i+1}")
                            st.write(article['summary'])
