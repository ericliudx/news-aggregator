import streamlit as st
from news_agent import NewsAgent


st.title("News Aggregator Agent")



api_key = st.text_input("Enter your NewsAPI key", type="password")
query = st.text_input("Search topic", "technology")

if st.button("Fetch News"):
  if not api_key:
    st.error("Please provide a NewsAPI Key")
  else: 
    agent = NewsAgent(api_key)
    articles = agent.get_summaries(query, limit=5)
    if not articles:
      st.warning("No articles found")
    for article in articles[:5]:
      st.subheader(article["title"])
      st.write(article["url"])
      st.write("**Summary:**", article["summary"])

if st.button("Test Articles"):
  if not api_key:
    st.error("Please provide a NewsAPI Key")
  else:
    st.warning("sigma sigma sigma")