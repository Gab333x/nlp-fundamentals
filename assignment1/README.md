# Assignment 1: Web Scraping & Regular Expressions

## Overview

This module focuses on foundational NLP techniques using web scraping and regular expressions for text extraction and cleaning.

## Notebooks

### 1. `regex_news_scraping.ipynb`

**Objectives:**
- Scrape 50+ news articles using Selenium
- Use regex to extract structured information
- Clean and normalize text data

**Key Tasks:**
1. Extract URLs from articles
2. Parse publication dates
3. Identify author names
4. Extract email addresses
5. Find phone numbers
6. Remove HTML tags and special characters
7. Identify organizations/companies
8. Clean whitespace and line breaks
9. Extract headlines and titles
10. Detect important events and incidents

**Technologies:**
- Selenium WebDriver
- Regular expressions (re module)
- BeautifulSoup for HTML parsing

### 2. `text_preprocessing.ipynb`

**Focus:** Advanced text cleaning and normalization techniques

**Topics Covered:**
- Stop word removal
- Stemming vs Lemmatization
- Case normalization
- Punctuation handling
- Tokenization strategies

### 3. `text_analysis.ipynb`

**Focus:** Pattern analysis and feature extraction from news text

**Topics Covered:**
- Statistical text analysis
- N-gram extraction
- Frequency distributions
- Pattern recognition

## Running the Code

```bash
# Make sure you're in the assignment1 directory
cd assignment1

# Start Jupyter
jupyter notebook

# Open and run notebooks in order:
# 1. regex_news_scraping.ipynb
# 2. text_preprocessing.ipynb
# 3. text_analysis.ipynb
```

## Prerequisites

```bash
pip install selenium webdriver-manager beautifulsoup4 pandas
```

## Common Issues

**ChromeDriver errors**: The notebook uses `webdriver-manager` to automatically download the correct ChromeDriver version.

**Scraping timeouts**: Increase wait times in the Selenium code if websites are slow to load.

## Key Learnings

- Selenium for dynamic content scraping
- Regex pattern design for text extraction
- HTML cleaning techniques
- Text normalization best practices

