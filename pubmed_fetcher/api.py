import requests

PUBMED_SEARCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PUBMED_FETCH_URL = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi"


def fetch_article_ids(query: str, max_results: int = 100):
    """Fetch PubMed article IDs for a given query."""
    params = {
        "db": "pubmed",
        "term": query,
        "retmode": "json",
        "retmax": max_results,
    }
    response = requests.get(PUBMED_SEARCH_URL, params=params)
    response.raise_for_status()
    return response.json().get("esearchresult", {}).get("idlist", [])


def fetch_article_details(article_ids: list):
    """Fetch article details from PubMed API using article IDs."""
    if not article_ids:
        return ""

    params = {
        "db": "pubmed",
        "id": ",".join(article_ids),
        "retmode": "xml"
    }
    response = requests.get(PUBMED_FETCH_URL, params=params)
    response.raise_for_status()
    return response.text  # Returns XML response


