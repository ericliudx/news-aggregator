import streamlit as st
from news_agent import fetch_news, summarize_article


st.title("News Aggregator Agent")

api_key = st.text_input("Enter your NewsAPI key", type="password")
query = st.text_input("Search topic", "technology")

if st.button("Fetch News"):
  if not api_key:
    st.error("Please provide a NewsAPI Key")
  else: 
    articles = fetch_news(api_key, query)
    if not articles:
      st.warning("No articles found")
    for article in articles[:5]:
      st.subheader(article.get('title', 'No Title'))
      st.write(article.get('url', ''))
      st.write("**Summary:**", summarize_article(article.get('content', '')))