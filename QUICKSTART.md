# 🚀 Quick Start Guide

Get started exploring NLP fundamentals in **5 minutes**!

## ⚡ Fastest Path

```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/nlp-fundamentals.git
cd nlp-fundamentals

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download dataset (for Part 2)
# Visit: https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset
# Download train.csv and test.csv
# Place in: classification/data/

# 4. Start Jupyter
jupyter notebook
```

## 📚 Recommended Learning Path

### Start Here: Part 1 - Web Scraping & Regex
1. Open `web-scraping/regex_news_scraping.ipynb`
2. Run cells to see Selenium scraping in action
3. Learn regex patterns for text extraction
4. Continue with preprocessing and analysis notebooks

**Time**: ~30-45 minutes

### Then: Part 2 - Traditional ML Classification
1. Ensure dataset is in `classification/data/`
2. Open `classification/news_classification.ipynb`
3. Follow the complete ML pipeline
4. Compare different classifiers

**Time**: ~45-60 minutes

### Optional: Production Scrapy Spider
```bash
cd classification/news_scrapper
scrapy crawl news -o output.json
```

**Time**: ~10 minutes

---

## 🎯 What You'll Learn

### Part 1: Web Scraping Foundations
- ✅ Web scraping with Selenium
- ✅ Regex for text extraction
- ✅ HTML cleaning
- ✅ Text normalization

### Part 2: Traditional Machine Learning
- ✅ EDA techniques
- ✅ TF-IDF, Word2Vec
- ✅ Logistic Regression, Random Forest
- ✅ Model evaluation
- ✅ Production scraping with Scrapy

---

## 🚨 Quick Troubleshooting

| Issue | Fix |
|-------|-----|
| ChromeDriver not found | Already handled by `webdriver-manager` |
| Dataset missing | Download from Kaggle link above |
| Memory error | Reduce sample size in notebooks |
| Scrapy not found | Run: `pip install scrapy` |

---

## 📊 Expected Results

### Part 1: Web Scraping
- 50+ scraped news articles
- Extracted structured data (URLs, dates, emails, etc.)
- Clean, normalized text ready for analysis

### Part 2: Classification
- 85-90% classification accuracy
- Beautiful word clouds per category
- Confusion matrix visualizations
- Trained models ready for deployment

---

## 🔄 Next Steps

After mastering the fundamentals:

1. **[Semantic News Search](https://github.com/YOUR_USERNAME/semantic-news-search)**
   - Sentence transformers
   - Vector databases
   
2. **[News RAG Chatbot](https://github.com/YOUR_USERNAME/news-rag-chatbot)**
   - LLM integration
   - Retrieval-Augmented Generation

---

## 💡 Pro Tips

1. **Read notebooks top-to-bottom** - They're designed as learning paths
2. **Experiment with parameters** - Change values, see what happens
3. **Check README files** in each module folder for details
4. **Start with small samples** - Test with 100 articles before full dataset

---

**Ready to dive into NLP fundamentals!** 📚✨

For full documentation, see [README.md](README.md)

