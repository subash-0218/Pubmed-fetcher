from lxml import etree


def parse_article_details(xml_data):
    """Parse article details from XML response."""
    root = etree.fromstring(xml_data.encode("utf-8"))
    articles = []

    for article in root.findall(".//PubmedArticle"):
        pmid = article.findtext(".//PMID")
        title = article.findtext(".//ArticleTitle")
        pub_date = article.findtext(".//PubDate/Year")

        authors = []
        companies = []

        for author in article.findall(".//Author"):
            affiliation = author.findtext(".//Affiliation")
            if affiliation and any(term in affiliation.lower() for term in ["pharma", "biotech", "laboratories"]):
                authors.append(author.findtext(".//LastName"))
                companies.append(affiliation)

        articles.append({
            "PubmedID": pmid,
            "Title": title,
            "Publication Date": pub_date,
            "Non-academic Author(s)": ", ".join(authors),
            "Company Affiliation(s)": ", ".join(companies),
        })

    return articles


# Test parsing
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

print(parse_article_details(xml_test))  # Should return a parsed dictionary

