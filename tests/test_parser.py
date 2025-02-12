from pubmed_fetcher.parser import parse_article_details


def test_parse_article_details():
    """Test parsing XML data."""
    xml_test = """<PubmedArticleSet>
        <PubmedArticle>
            <MedlineCitation>
                <PMID>123456</PMID>
                <Article>
                    <ArticleTitle>Test Paper</ArticleTitle>
                    <Journal>
                        <PubDate>
                            <Year>2024</Year>
                        </PubDate>
                    </Journal>
                    <AuthorList>
                        <Author>
                            <LastName>Smith</LastName>
                            <Affiliation>ABC Biotech</Affiliation>
                        </Author>
                    </AuthorList>
                </Article>
            </MedlineCitation>
        </PubmedArticle>
    </PubmedArticleSet>"""

    result = parse_article_details(xml_test)
    assert isinstance(result, list)
    assert result[0]["PubmedID"] == "123456"
    assert result[0]["Title"] == "Test Paper"

