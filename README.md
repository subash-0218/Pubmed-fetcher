# PubMed Paper Fetcher 
# Overview
The PubMed Paper Fetcher is a Python-based command-line tool designed to automate the retrieval of research papers from PubMed based on a user-specified query. The program filters papers where at least one author is affiliated with a pharmaceutical or biotech company and exports the results into a CSV file for further analysis.This tool eliminates the need for manual searching and filtering, making it useful for researchers, analysts, and professionals who need to quickly extract relevant biomedical literature.

# Features
Retrieves research papers from PubMed's E-utilities API
Filters authors based on affiliations with pharmaceutical/biotech companies
Exports results to CSV for structured storage
Command-line interface (CLI) for easy user interaction
Debug mode for detailed execution logs
Error handling and retry mechanisms for API failures

# Installation
Python 3.8+ (Check with python --version)
Poetry for dependency management (Install with pip install poetry

# Clone the Repository
git clone https://github.com/Subash-0218/pubmed-fetcher.git
cd pubmed-fetcher

# Project Structure
pubmed-fetcher/
│── pubmed_fetcher/       # Main package
│   │── __init__.py       # Package initialization
│   │── api.py            # Handles PubMed API requests
│   │── parser.py         # Parses XML responses
│   │── cli.py            # CLI functionality
│
│── tests/                # Unit tests
│   │── test_api.py       # Tests API interactions
│   │── test_parser.py    # Tests XML parsing
│
│── pyproject.toml        # Poetry configuration
│── README.md             # Project documentation
│── .gitignore            # Ignored files
│── results.csv           # Sample output file

# How It Works
1. Fetching Research Papers
2. Retrieving Article Details
3. Filtering Non-Academic Authors
4. Storing Results in CSV



