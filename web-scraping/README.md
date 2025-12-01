# Part 1: Web Scraping & Regular Expressions

## Overview

This module explores foundational NLP techniques using web scraping and regular expressions for text extraction and cleaning from news articles.

## Notebooks

### 1. `regex_news_scraping.ipynb`

**Focus:** Web scraping and regex-based information extraction

**What's Covered:**
- Scraping 50+ news articles using Selenium WebDriver
- Regex patterns for structured data extraction
- Text cleaning and normalization

**Key Techniques:**
1. URL extraction from article text
2. Publication date parsing with regex
3. Author name identification
4. Email address extraction
5. Phone number detection
6. HTML tag and special character removal
7. Organization/company name recognition
8. Whitespace and line break normalization
9. Headline and title extraction
10. Event and incident detection

**Technologies:**
- Selenium WebDriver for browser automation
- Python's `re` module for regex
- BeautifulSoup for HTML parsing

### 2. `text_preprocessing.ipynb`

**Focus:** Advanced text cleaning and normalization

**Topics:**
- Stop word removal strategies
- Stemming vs Lemmatization
- Case normalization
- Punctuation handling
- Tokenization approaches

### 3. `text_analysis.ipynb`

**Focus:** Pattern analysis and statistical exploration

**Topics:**
- Statistical text analysis
- N-gram extraction
- Frequency distributions
- Pattern recognition in news text

## Quick Start

```bash
# Navigate to this directory
cd web-scraping

# Start Jupyter
jupyter notebook

# Run notebooks in order:
# 1. regex_news_scraping.ipynb
# 2. text_preprocessing.ipynb
# 3. text_analysis.ipynb
```

## Prerequisites

```bash
pip install selenium webdriver-manager beautifulsoup4 pandas matplotlib
```

## Common Issues

**ChromeDriver errors**: The notebooks use `webdriver-manager` to automatically download the correct ChromeDriver version for your system.

**Scraping timeouts**: If websites are slow to load, increase wait times in the Selenium configuration.

**Rate limiting**: Implement delays between requests to respect website policies.

## Key Takeaways

- Selenium enables scraping of JavaScript-rendered content
- Regex patterns provide powerful text extraction capabilities
- HTML cleaning is essential for downstream NLP tasks
- Text normalization improves analysis quality
- Production scrapers need robust error handling

## Next Steps

After completing this module, move to **Part 2: Traditional ML Classification** to apply machine learning to the cleaned text data.
