import argparse
import csv
from pubmed_fetcher.api import fetch_article_ids, fetch_article_details
from pubmed_fetcher.parser import parse_article_details


def main():
    parser = argparse.ArgumentParser(description="Fetch research papers from PubMed")
    parser.add_argument("query", type=str, help="Search query")
    parser.add_argument("-f", "--file", type=str, help="Output CSV filename")
    parser.add_argument("-d", "--debug", action="store_true", help="Enable debug mode")

    args = parser.parse_args()

    if args.debug:
        print("Fetching article IDs...")
    article_ids = fetch_article_ids(args.query)

    if args.debug:
        print(f"Found {len(article_ids)} articles. Fetching details...")

    xml_data = fetch_article_details(article_ids)
    articles = parse_article_details(xml_data)

    if args.file:
        with open(args.file, "w", newline="",  encoding="utf-8",errors="replace") as f:
            writer = csv.DictWriter(f, fieldnames=articles[0].keys())
            writer.writeheader()
            writer.writerows(articles)
        print(f"Results saved to {args.file}")
    else:
        print(articles)


if __name__ == "__main__":
    main()

