import urllib.request
import urllib.parse
import xml.etree.ElementTree as ET

def fetch_arxiv(query):
    print(f"--- Arxiv Search: {query} ---")
    url = f"http://export.arxiv.org/api/query?search_query=all:{urllib.parse.quote(query)}&start=0&max_results=5&sortBy=submittedDate&sortOrder=desc"
    req = urllib.request.Request(url)
    resp = urllib.request.urlopen(req)
    xml_data = resp.read().decode("utf-8")
    root = ET.fromstring(xml_data)
    namespace = {'atom': 'http://www.w3.org/2005/Atom'}
    for entry in root.findall('atom:entry', namespace):
        title = entry.find('atom:title', namespace).text.replace('\n', ' ').strip()
        published = entry.find('atom:published', namespace).text
        link = entry.find('atom:id', namespace).text
        print(f"- {title} ({published}) {link}")

fetch_arxiv("LLM Agent")
