import pytest
from pubmed_fetcher.api import fetch_article_ids

def test_fetch_article_ids():
    """Test fetching article IDs from PubMed."""
    query = "cancer"
    result = fetch_article_ids(query)
    assert isinstance(result, list)  # Ensure the output is a list
    assert len(result) > 0  # Ensure we get at least one article ID

