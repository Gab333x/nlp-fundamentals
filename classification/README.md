# Part 2: Traditional Machine Learning Classification

## Overview

This module explores traditional machine learning approaches to news article classification, demonstrating the complete ML pipeline from EDA through deployment.

## Contents

### 1. `news_classification.ipynb`

**Complete ML Pipeline Implementation**

#### Phase 1: Data Loading & EDA
- Load AG News dataset (120K training, 7.6K test samples)
- Analyze class distributions
- Generate word clouds for each category
- Compute text statistics
- Identify data quality issues

#### Phase 2: Text Preprocessing
- Lowercase conversion
- Stop word removal
- Special character cleaning
- Text normalization
- Duplicate detection

#### Phase 3: Feature Engineering
Multiple encoding approaches:
- **TF-IDF**: Term frequency-inverse document frequency weighting
- **CountVectorizer**: Traditional bag-of-words
- **Word2Vec**: Dense semantic embeddings

#### Phase 4: Model Training
Compare multiple classifiers:
- Logistic Regression (typically best performer)
- Random Forest
- Support Vector Machine (optional)

#### Phase 5: Evaluation
- Accuracy, Precision, Recall, F1-Score
- Confusion matrix visualization
- Per-class performance analysis
- Model comparison tables

#### Phase 6: Real-World Application
- Apply trained models to scraped news data
- Generate predictions on custom articles
- Evaluate generalization performance

### 2. `news_scrapper/` - Scrapy Project

**Production-Grade Web Scraping Framework**

#### Structure
```
news_scrapper/
├── scrapy.cfg              # Project configuration
└── news/
    ├── __init__.py
    ├── items.py            # Data models/schemas
    ├── middlewares.py      # Request/response processing
    ├── pipelines.py        # Data cleaning pipeline
    ├── settings.py         # Crawler settings
    └── spiders/
        └── news.py         # News spider implementation
```

#### Usage

```bash
cd news_scrapper

# Scrape to JSON
scrapy crawl news -o output.json

# Scrape to CSV
scrapy crawl news -o scraped_data.csv

# With custom settings
scrapy crawl news -s DOWNLOAD_DELAY=2 -s CONCURRENT_REQUESTS=1 -o output.json
```

#### Features
- Multi-source news scraping
- Automatic rate limiting
- Robust error handling
- Data validation pipeline
- Duplicate detection
- HTML content cleaning

### 3. `data/` - AG News Dataset

**Dataset Specifications:**
- **Source**: [Kaggle - AG News Classification](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)
- **Training**: 120,000 samples
- **Test**: 7,600 samples
- **Classes**: 4 balanced categories
  - 1: World News
  - 2: Sports
  - 3: Business
  - 4: Sci/Tech

**Download Steps:**
1. Visit the Kaggle dataset page
2. Download `train.csv` and `test.csv`
3. Place in this `data/` directory

**Format:**
```csv
Class Index, Title, Description
```

## Getting Started

### Step 1: Setup

```bash
# Install all dependencies
pip install -r ../requirements.txt

# Download dataset from Kaggle
# Place train.csv and test.csv in data/ directory
```

### Step 2: Run Classification Pipeline

```bash
jupyter notebook news_classification.ipynb
```

### Step 3: Run Production Scraper (Optional)

```bash
cd news_scrapper
scrapy crawl news -o my_news.json
```

## Expected Results

### Classification Performance
- **Logistic Regression + TF-IDF**: 85-90% accuracy
- **Random Forest**: 80-85% accuracy
- **Word2Vec + Logistic Regression**: 82-87% accuracy

### Visualizations
- Class distribution bar charts
- Word clouds (4 categories showing distinctive terms)
- Confusion matrix heatmaps
- Learning curves (optional)

## Technologies

- **scikit-learn**: ML algorithms and evaluation
- **pandas**: Data manipulation
- **matplotlib/seaborn**: Visualization
- **wordcloud**: Word cloud generation
- **scrapy**: Production web scraping
- **gensim**: Word2Vec embeddings
- **nltk**: Text preprocessing

## Troubleshooting

**Dataset not found**: Download from Kaggle and ensure files are in `data/`

**Memory issues**: Use smaller sample sizes for experimentation

**Scrapy errors**: Check `settings.py` for proper configuration

**Import errors**: Ensure all packages in `requirements.txt` are installed

## Key Learnings

- Traditional ML pipelines for text classification
- Feature engineering is crucial for performance
- TF-IDF often outperforms more complex encodings
- Production scrapers require careful rate limiting
- Model evaluation requires multiple metrics
- Real-world data differs from benchmark datasets

## Next Steps

After mastering traditional approaches, explore modern techniques:
- **Sentence Transformers** for semantic similarity
- **Pre-trained Language Models** (BERT, RoBERTa)
- **Few-shot Learning** with LLMs
- **RAG Systems** for question answering

See the **[Semantic News Search](https://github.com/YOUR_USERNAME/semantic-news-search)** and **[News RAG Chatbot](https://github.com/YOUR_USERNAME/news-rag-chatbot)** projects for advanced implementations.
