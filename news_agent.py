import requests
from transformers import pipeline

summarizer = pipeline("summarization", model = "facebook/bart-large-cnn")

def fetch_news (api_key, query="technology"):
  #fetching news articles with NewsAPI
  url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
  response = requests.get(url)
  return response.json().get("articles", [])

def summarize_article (text):
  if not text:
    return "No content available"
  if len(text) < 100:
    return text
  summary = summarizer(text, max_length=100, min_length=30, do_sample=False)
  print(summary)
  return summary[0]['summary_text'] 
