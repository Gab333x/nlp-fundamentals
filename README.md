# 📚 NLP Fundamentals

A hands-on exploration of foundational Natural Language Processing techniques, from web scraping and regex-based text extraction to traditional machine learning classifiers. This project demonstrates core NLP skills through practical implementations, serving as building blocks for advanced applications.

## 🎯 What This Repository Demonstrates

### Core NLP Skills
- **Web Scraping**: Selenium-based news article extraction
- **Regular Expressions**: Pattern matching for text extraction and cleaning
- **Text Preprocessing**: Stop word removal, normalization, cleaning
- **Exploratory Data Analysis**: Class distributions, word clouds, statistical analysis
- **Feature Engineering**: TF-IDF, CountVectorizer, Word2Vec embeddings
- **Traditional ML**: Logistic Regression, RandomForest, SVM classifiers
- **Model Evaluation**: Accuracy, Precision, Recall, F1-Score, Confusion Matrix
- **Scrapy Framework**: Production-grade web scraping

## 🏗️ Repository Structure

```
nlp-fundamentals/
├── README.md                           # This file
├── requirements.txt                    # Python dependencies
├── web-scraping/                       # Part 1: Regex & Web Scraping
│   ├── regex_news_scraping.ipynb      # Selenium + regex extraction
│   ├── text_preprocessing.ipynb       # Text cleaning techniques
│   └── text_analysis.ipynb            # Pattern analysis
├── classification/                     # Part 2: Traditional ML Classification
│   ├── news_classification.ipynb      # Full ML pipeline
│   ├── news_scrapper/                 # Scrapy project
│   │   ├── news/                      # Spider & pipeline code
│   │   └── scrapy.cfg                 # Scrapy configuration
│   └── data/                          # AG News dataset
│       ├── train.csv                  # 120,000 news articles (download)
│       └── test.csv                   # 7,600 news articles (download)
└── docs/                              # Additional documentation
```

## 📖 Module Overview

### Part 1: Web Scraping & Regex

**Skills Demonstrated:**
- Selenium WebDriver for dynamic content scraping
- Regex patterns for URL, date, email, phone extraction
- HTML tag removal and text cleaning
- Named entity recognition (organizations, events)
- Whitespace normalization

**Notebooks:**
1. **`regex_news_scraping.ipynb`**
   - Scrape 50+ news articles using Selenium
   - Extract URLs, dates, authors, emails, phone numbers
   - Clean HTML tags and special characters
   - Identify organizations and events

2. **`text_preprocessing.ipynb`**
   - Advanced text cleaning techniques
   - Stop word removal
   - Stemming and lemmatization
   - Text normalization

3. **`text_analysis.ipynb`**
   - Pattern analysis in news text
   - Statistical text analysis
   - Feature extraction

**Key Technologies:**
- `selenium` - Browser automation
- `beautifulsoup4` - HTML parsing
- `re` (regex) - Pattern matching
- `pandas` - Data manipulation

---

### Part 2: Traditional ML Classification

**Skills Demonstrated:**
- EDA with visualizations (word clouds, distributions)
- Text vectorization (TF-IDF, CountVectorizer, Word2Vec)
- ML pipeline construction
- Multi-classifier comparison
- Model evaluation and selection
- Scrapy for production web scraping

**Notebook:**
**`news_classification.ipynb`**
- Load and clean AG News dataset (120K training samples)
- Exploratory Data Analysis:
  - Class distribution visualization
  - Word clouds per category
  - Text length statistics
- Text preprocessing pipeline
- Feature engineering:
  - TF-IDF vectorization
  - CountVectorizer
  - Word2Vec embeddings
- Train multiple classifiers:
  - Logistic Regression
  - Random Forest
  - SVM (optional)
- Model comparison and selection
- Evaluation metrics:
  - Accuracy, Precision, Recall, F1-Score
  - Confusion matrix visualization
- Apply trained model to scraped news data

**Scrapy Project:**
**`news_scrapper/`**
- Production-grade news scraping framework
- Custom spider for multiple news sources
- Item pipelines for data cleaning
- Configurable settings
- Output to JSON/CSV

**Dataset:**
- **AG News Classification Dataset** (Kaggle)
- 4 categories: World, Sports, Business, Sci/Tech
- 120,000 training samples
- 7,600 test samples

**Key Technologies:**
- `scikit-learn` - ML algorithms
- `pandas` & `numpy` - Data processing
- `matplotlib` & `seaborn` - Visualization
- `wordcloud` - Word cloud generation
- `scrapy` - Web scraping framework
- `gensim` - Word2Vec embeddings

---

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- Jupyter Notebook
- Chrome browser (for Selenium)

### Installation

```bash
# Clone the repository
git clone https://github.com/YOUR_USERNAME/nlp-fundamentals.git
cd nlp-fundamentals

# Create virtual environment (recommended)
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Download AG News dataset (if not included)
# Place train.csv and test.csv in assignment2/data/
```

### Running the Notebooks

```bash
# Start Jupyter
jupyter notebook

# Navigate to desired module folder
# Open and run notebooks in order
```

### Running the Scrapy Spider

```bash
cd classification/news_scrapper

# Run the news spider
scrapy crawl news -o output.json

# Or output to CSV
scrapy crawl news -o output.csv
```

---

## 📊 Key Results

### Web Scraping & Regex
- Successfully scraped 50+ news articles using Selenium
- Extracted structured data using regex patterns
- Cleaned and normalized text for downstream analysis

### Traditional ML Classification
- **Best Model**: [Your best classifier here]
- **Test Accuracy**: [Your accuracy here]
- **F1-Score**: [Your F1 score here]
- Successfully classified scraped news articles into 4 categories

---

## 🎓 Learning Outcomes

### Technical Skills Acquired
1. **Web Scraping**
   - Selenium for dynamic content
   - Scrapy for production scraping
   - Handling different page structures

2. **Text Processing**
   - Regex pattern design
   - Text normalization techniques
   - HTML/special character cleaning

3. **Feature Engineering**
   - TF-IDF weighting
   - Bag-of-words representation
   - Word embeddings (Word2Vec)

4. **Machine Learning**
   - ML pipeline construction
   - Hyperparameter tuning
   - Model comparison
   - Evaluation metrics interpretation

5. **Data Analysis**
   - EDA techniques
   - Visualization best practices
   - Statistical analysis

### Best Practices Learned
- Clean code organization
- Reproducible research with notebooks
- Documentation and commenting
- Error handling in scrapers
- Pipeline-based ML workflows

---

## 🔄 Progression Path

This repository is part of a 3-project NLP learning journey:

1. **NLP Fundamentals** (This repo) ⭐
   - Regex, scraping, traditional ML
   - Foundational skills

2. **[Semantic News Search](https://github.com/YOUR_USERNAME/semantic-news-search)** ⭐
   - Sentence transformers
   - Vector databases (Qdrant)
   - Semantic similarity

3. **[News RAG Chatbot](https://github.com/YOUR_USERNAME/news-rag-chatbot)** ⭐⭐
   - Retrieval-Augmented Generation
   - LLM integration (Ollama/OpenAI)
   - Production deployment

**Progression:** Traditional NLP → Modern Embeddings → LLM Applications

---

## 🛠️ Technologies Used

### Core Libraries
- **Web Scraping**: `selenium`, `scrapy`, `beautifulsoup4`
- **Text Processing**: `re`, `nltk`, `spacy`
- **Machine Learning**: `scikit-learn`, `gensim`
- **Data Analysis**: `pandas`, `numpy`
- **Visualization**: `matplotlib`, `seaborn`, `wordcloud`

### Development Tools
- Jupyter Notebook
- ChromeDriver (Selenium)
- Git version control

---

## 📚 Datasets

### AG News Classification Dataset
- **Source**: [Kaggle - AG News](https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset)
- **Size**: 127,600 total samples
- **Classes**: 4 (World, Sports, Business, Sci/Tech)
- **Format**: CSV with title and description
- **License**: Public domain

**Download Instructions:**
1. Visit the Kaggle link above
2. Download `train.csv` and `test.csv`
3. Place in `classification/data/` directory

---

## 🚨 Troubleshooting

### Selenium Issues

**Problem**: Chrome driver not found

**Solution**:
```bash
pip install webdriver-manager
```

The notebooks use `webdriver-manager` to auto-download the correct ChromeDriver.

### Scrapy Issues

**Problem**: Module not found

**Solution**:
```bash
pip install scrapy
```

### Dataset Issues

**Problem**: Dataset files not found

**Solution**: Download from Kaggle and place in `classification/data/`:
- `train.csv`
- `test.csv`

### Memory Issues

**Problem**: Notebook crashes with large dataset

**Solution**: Reduce sample size in the notebook or use more RAM

---

## 📈 Future Enhancements

### Potential Improvements
- [ ] Add more text preprocessing techniques (POS tagging, dependency parsing)
- [ ] Implement deep learning classifiers (CNN, LSTM)
- [ ] Add cross-validation for robust evaluation
- [ ] Expand regex patterns for more entity types
- [ ] Add multilingual support
- [ ] Implement active learning
- [ ] Create web dashboard for results

---

## 👤 About This Project

This project explores foundational NLP techniques through hands-on implementation, demonstrating:
- Core text processing and extraction skills
- Traditional machine learning approaches
- Production-grade web scraping
- Clean, reproducible code organization
- Best practices in NLP pipelines

---

## 📝 License

This project is for educational purposes.

Dataset: AG News Classification Dataset (Public Domain)

---

## 🔗 Related Projects

- **[Semantic News Search](https://github.com/YOUR_USERNAME/semantic-news-search)** - Vector-based news search
- **[News RAG Chatbot](https://github.com/YOUR_USERNAME/news-rag-chatbot)** - RAG-powered Q&A system

---

**Building strong NLP foundations for advanced applications** 🚀

