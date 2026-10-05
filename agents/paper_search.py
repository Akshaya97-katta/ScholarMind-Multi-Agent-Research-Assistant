import requests
import xml.etree.ElementTree as ET


def search_papers(topic):
    url = (
        f"http://export.arxiv.org/api/query?"
        f"search_query=all:{topic}"
        f"&start=0"
        f"&max_results=5"
    )

    response = requests.get(url)
    root = ET.fromstring(response.content)

    papers = []

    namespace = {
        "atom": "http://www.w3.org/2005/Atom"
    }

    for entry in root.findall("atom:entry", namespace):
        title = entry.find("atom:title", namespace).text.strip()

        abstract = entry.find("atom:summary", namespace).text.strip()

        authors = []
        for author in entry.findall("atom:author", namespace):
            name = author.find("atom:name", namespace).text
            authors.append(name)

        published = entry.find("atom:published", namespace).text
        link = entry.find("atom:id", namespace).text

        papers.append({
            "title": title,
            "abstract": abstract,
            "authors": authors,
            "published": published,
            "link": link
        })

    return papers