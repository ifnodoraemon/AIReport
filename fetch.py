import urllib.request
import json
import datetime

def fetch_hn(query):
    url = f"https://hn.algolia.com/api/v1/search_by_date?query={query}&tags=story"
    req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    resp = urllib.request.urlopen(req)
    data = json.loads(resp.read().decode("utf-8"))
    print(f"--- HN Search: {query} ---")
    for hit in data["hits"][:5]:
        print(f"- {hit['title']} ({hit['created_at']}) {hit.get('url')}")

try:
    fetch_hn("OpenAI")
    fetch_hn("Anthropic")
    fetch_hn("DeepMind")
    fetch_hn("LLM Agent")
except Exception as e:
    print("Error:", e)
