# 🚀 Quick Start Guide

Get started with NLP fundamentals in **5 minutes**!

## ⚡ Fastest Path

```bash
# 1. Clone repository
git clone https://github.com/YOUR_USERNAME/nlp-fundamentals.git
cd nlp-fundamentals

# 2. Install dependencies
pip install -r requirements.txt

# 3. Download dataset (for Assignment 2)
# Visit: https://www.kaggle.com/datasets/amananandrai/ag-news-classification-dataset
# Download train.csv and test.csv
# Place in: assignment2/data/

# 4. Start Jupyter
jupyter notebook
```

## 📚 Recommended Learning Path

### Start Here: Assignment 1
1. Open `assignment1/regex_news_scraping.ipynb`
2. Run cells to see Selenium scraping in action
3. Learn regex patterns for text extraction
4. Continue with preprocessing and analysis notebooks

**Time**: ~30-45 minutes

### Then: Assignment 2
1. Ensure dataset is in `assignment2/data/`
2. Open `assignment2/news_classification.ipynb`
3. Follow the complete ML pipeline
4. Compare different classifiers

**Time**: ~45-60 minutes

### Optional: Scrapy Spider
```bash
cd assignment2/news_scrapper
scrapy crawl news -o output.json
```

**Time**: ~10 minutes

---

## 🎯 What You'll Learn

### Assignment 1: Foundations
- ✅ Web scraping with Selenium
- ✅ Regex for text extraction
- ✅ HTML cleaning
- ✅ Text normalization

### Assignment 2: Machine Learning
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

### Assignment 1
- 50+ scraped news articles
- Extracted structured data (URLs, dates, emails, etc.)
- Clean, normalized text

### Assignment 2
- 85-90% classification accuracy
- Beautiful word clouds per category
- Confusion matrix visualizations
- Trained model ready for deployment

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

1. **Read notebooks top-to-bottom** - They're designed as tutorials
2. **Experiment with parameters** - Change values, see what happens
3. **Check README files** in each assignment folder for details
4. **Start with small samples** - Test with 100 articles before full dataset

---

**Ready to dive into NLP fundamentals!** 📚✨

For full documentation, see [README.md](README.md)

