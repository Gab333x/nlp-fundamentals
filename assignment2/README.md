# Assignment 2: Traditional Machine Learning Classification

## Overview

This module demonstrates traditional machine learning techniques for news classification using the AG News dataset.

## Contents

### 1. `news_classification.ipynb`

**Complete ML Pipeline:**

#### Phase 1: Data Loading & EDA
- Load AG News dataset (120K train, 7.6K test)
- Class distribution analysis
- Generate word clouds per category
- Text length statistics
- Missing value analysis

#### Phase 2: Text Preprocessing
- Lowercase conversion
- Stop word removal
- Special character cleaning
- Text normalization
- Deduplication

#### Phase 3: Feature Engineering
Try multiple encoding methods:
- **TF-IDF**: Term frequency-inverse document frequency
- **CountVectorizer**: Bag-of-words representation
- **Word2Vec**: Dense word embeddings

#### Phase 4: Model Training
Train and compare multiple classifiers:
- Logistic Regression
- Random Forest
- Support Vector Machine (optional)

#### Phase 5: Evaluation
- Accuracy, Precision, Recall, F1-Score
- Confusion matrix visualization
- Per-class performance analysis
- Model comparison

#### Phase 6: Application
- Apply trained model to scraped news data
- Generate predictions
- Evaluate on custom dataset

### 2. `news_scrapper/` - Scrapy Project

**Production-grade web scraping framework**

#### Project Structure
```
news_scrapper/
├── scrapy.cfg              # Scrapy configuration
└── news/
    ├── __init__.py
    ├── items.py            # Data models
    ├── middlewares.py      # Request/response processing
    ├── pipelines.py        # Data cleaning pipeline
    ├── settings.py         # Scrapy settings
    └── spiders/
        ├── __init__.py
        └── news.py         # News spider implementation
```

#### Running the Spider

```bash
cd news_scrapper

# Scrape and output to JSON
scrapy crawl news -o output.json

# Scrape and output to CSV
scrapy crawl news -o scraped_data.csv

# Custom settings
scrapy crawl news -s DOWNLOAD_DELAY=2 -o output.json
```

#### Spider Features
- Multiple news source support
- Automatic rate limiting
- Robust error handling
- Data validation pipeline
- Duplicate detection
- HTML cleaning

### 3. `data/` - AG News Dataset

**Dataset Details:**
- **Source**: [Kaggle - AG News Classification](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)
- **Training samples**: 120,000
- **Test samples**: 7,600
- **Categories**: 4
  - 1: World
  - 2: Sports
  - 3: Business
  - 4: Sci/Tech

**Download Instructions:**
1. Visit the Kaggle link
2. Download `train.csv` and `test.csv`
3. Place in this `data/` directory

**Format:**
```
Class Index, Title, Description
```

## Running the Code

### Step 1: Setup

```bash
# Install dependencies
pip install -r ../requirements.txt

# Download dataset
# Place train.csv and test.csv in data/ directory
```

### Step 2: Run Classification Notebook

```bash
jupyter notebook news_classification.ipynb
```

### Step 3: Run Scraper (Optional)

```bash
cd news_scrapper
scrapy crawl news -o output.json
```

## Expected Results

### Classification Performance
- **Logistic Regression**: 85-90% accuracy
- **Random Forest**: 80-85% accuracy
- **Best Model**: Typically Logistic Regression with TF-IDF

### Visualizations
- Class distribution bar charts
- Word clouds (4 categories)
- Confusion matrix heatmaps
- Feature importance plots

## Key Technologies

- **scikit-learn**: ML algorithms
- **pandas**: Data manipulation
- **matplotlib/seaborn**: Visualization
- **wordcloud**: Word cloud generation
- **scrapy**: Web scraping
- **gensim**: Word2Vec embeddings

## Troubleshooting

**Dataset not found**: Download from Kaggle and place in `data/`

**Memory issues**: Reduce sample size or use sparse matrices

**Scrapy errors**: Check `settings.py` for configuration

**Visualization issues**: Ensure matplotlib backend is set correctly

## Key Learnings

- Traditional ML pipeline construction
- Feature engineering for text
- Model comparison and selection
- Production web scraping with Scrapy
- Evaluation metrics interpretation
- Handling imbalanced classes (if present)

## Next Steps

After mastering traditional ML, explore:
- Deep learning classifiers (CNN, LSTM)
- Transformer models (BERT, RoBERTa)
- Few-shot learning
- Active learning strategies

