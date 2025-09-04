import requests
from transformers import pipeline


class NewsAgent:
  def __init__(self, api_key, query="technology", model="sshleifer/tiny-distilbart-cnn-6-6"):
    self.api_key = api_key
    self.summarizer = pipeline("summarization", model=model)
    self.query = query

  def fetch_news (api_key, query="technology"):
    #fetching news articles with NewsAPI
    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    return response.json().get("articles", [])

  def summarize_article (self, text):
    if not text:
      return "No content available"
    if len(text) < 100:
      return text
    summary = self.summarizer(text, max_length=100, min_length=30, do_sample=False)
    print(summary[0])
    return summary[0]['summary_text'] 

  def get_summaries(self, query, limit):
    articles = self.fetch_news(query)
    results = []
    for article in articles[:limit]:
      content = article.get("content") or article.get("description")
      summary = self.summarize.content()
      results.append({
        "title": article["title"],
        "url": article["url"],
        "summary": summary
      })
      return results

