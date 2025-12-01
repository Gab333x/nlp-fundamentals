import scrapy
import hashlib
import requests
import re
from urllib.parse import urlparse
from scrapy.http import Request
from scrapy.exceptions import NotConfigured
from scrapy.selector import Selector
from scrapy.linkextractors import LinkExtractor

class NewsSpider(scrapy.Spider):
    name = 'news'
    
    # --- Corrected allowed_domains ---
    allowed_domains = [
        "reuters.com",
        "bloomberg.com",
        "forbes.com",
        "businessinsider.com",
        "marketwatch.com",
        "wsj.com",
        "ft.com",
        "cnbc.com",
        "economist.com",
        "yahoo.com",
        "investing.com",
        "cnn.com",
        "businessweek.com",
        "moneymorning.com",
        "nasdaq.com",
        "seekingalpha.com",
        "theguardian.com",
        "republicworld.com",
        "thefinancialbrand.com",
        "morningstar.com",
        "nytimes.com",
        "npr.org",
        "bbc.com",
        "washingtonpost.com",
        "usatoday.com",
        "foxbusiness.com",
        "qz.com",
        "axios.com",
        "apnews.com",
        "politico.com",
    ]

    # --- Specific start_urls ---
    start_urls = [
        "https://www.reuters.com",
        "https://www.bloomberg.com",
        "https://www.forbes.com",
        "https://www.businessinsider.com",
        "https://www.marketwatch.com",
        "https://www.wsj.com",
        "https://www.ft.com",
        "https://www.cnbc.com",
        "https://www.economist.com",
        "https://finance.yahoo.com",
        "https://www.investing.com",
        "https://www.cnn.com/business",
        "https://www.businessweek.com",
        "https://moneymorning.com",
        "https://www.nasdaq.com",
        "https://seekingalpha.com",
        "https://www.theguardian.com/uk/business",
        "https://www.republicworld.com/business",
        "https://thefinancialbrand.com",
        "https://www.morningstar.com",
        "https://www.nytimes.com/section/business",
        "https://www.npr.org/sections/business/",
        "https://www.bbc.com/business",
        "https://www.washingtonpost.com/business/",
        "https://www.usatoday.com/money/",
        "https://www.foxbusiness.com/",
        "https://qz.com/",
        "https://www.axios.com/business",
        "https://apnews.com/hub/business",
        "https://www.politico.com/economy"
    ]

    custom_settings = {
        'FEED_FORMAT': 'json',
        'FEED_URI': 'output.json',
        'DOWNLOAD_DELAY': 1, 
        'CONCURRENT_REQUESTS_PER_DOMAIN': 8,
        'ROBOTSTXT_OBEY': False, 
        'AUTOTHROTTLE_ENABLED': True,
        'USER_AGENT': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        
        # This tells the spider to crawl 3 links deep.
        'DEPTH_LIMIT': 3,
    }

    # Better heuristic regex
    article_pattern = re.compile(r'/\d{4}/\d{2}/\d{2}/|/article/|/news/|/story/|/[a-z0-9-]{30,}\.html$')
    
    # Regex for links to IGNORE
    ignore_pattern = re.compile(r'/(login|register|subscribe|privacy|terms|about|contact|shop|careers|video|gallery|live|search)')

    def start_requests(self):
        for url in self.start_urls:
            yield Request(url, callback=self.parse)

    # Rewritten 'parse' method for recursive crawling
    def parse(self, response):
        try:
            current_domain = urlparse(response.url).netloc.replace('www.', '')

            # 1. Parse this page for articles
            yield from self.parse_article_if_matches(response)

            # 2. Find all links on the page and follow them
            all_links = response.css('a::attr(href)').getall()
            for link in all_links:
                if not link:
                    continue
                
                full_link = response.urljoin(link)
                link_domain = urlparse(full_link).netloc.replace('www.', '')

                # Only follow the link if it's on the SAME domain
                # and doesn't match an "ignore" pattern
                if link_domain == current_domain and not self.ignore_pattern.search(full_link):
                    # If it looks like an article, send it to parse_article
                    if self.article_pattern.search(full_link):
                        yield response.follow(full_link, callback=self.parse_article)
                    # Otherwise, send it back to 'parse' to crawl deeper
                    else:
                        yield response.follow(full_link, callback=self.parse)
                        
        except Exception as e:
            self.logger.error(f"Error parsing {response.url}: {e}")

    def parse_article_if_matches(self, response):
        """
        Helper function to check if the *current* page is an article
        and yield its data if it is.
        """
        title_check = response.xpath('//meta[@property="og:title"]/@content').get()
        if title_check:
             yield from self.parse_article(response)
        
    def parse_article(self, response):
        try:
            title = self.extract_title(response)
            
            if title == "No Title Found" or not title:
                return

            article_text = self.extract_article_text(response)
            if not article_text or len(article_text) < 200: # Skip if text is too short
                self.logger.warning(f"No/short article text found for {response.url}")
                return

            cleaned_title = self.clean_text(title)
            article_id = hashlib.md5(cleaned_title.encode('utf-8')).hexdigest()

            author = self.extract_author(response)
            date = self.extract_date(response)
            summary = self.extract_summary(response)

            yield {
                'id': article_id,
                'url': response.url,
                'title': cleaned_title,
                'text': article_text,
                'author': author,
                'date': date,
                'summary': summary,
            }
        except Exception as e:
            self.logger.error(f"Error parsing article {response.url}: {e}")

    # --- More robust "Selector Chains" ---

    def extract_title(self, response):
        """ Extracts the title using a fallback chain. """
        title = response.xpath('//meta[@property="og:title"]/@content').get()
        if not title:
            title = response.css('h1::text').get()
        if not title:
            title = response.css('title::text').get()
        return self.clean_text(title) or "No Title Found"

    def extract_article_text(self, response):
        """ Extracts the main content from various common article containers. """
        selectors = [
            'div.article-body p::text',
            'div.entry-content p::text',
            'article p::text',
            'div.article-content p::text',
            'div.story-content p::text',
            'div.post-content p::text',
            'section[itemprop="articleBody"] p::text'
        ]
        article_text = ' '.join(response.css(', '.join(selectors)).getall()).strip()
        
        if not article_text:
             article_text = ' '.join(response.css('article p::text').getall()).strip()
             
        if not article_text:
            # More generic, but risky. Let's scope it to common divs
            article_text = ' '.join(response.css('div[class*="article"] p::text, div[class*="story"] p::text, div[id*="article"] p::text').getall()).strip()

        return self.clean_text(article_text)

    def extract_author(self, response):
        """ Extracts the author using a fallback chain. """
        author = response.xpath('//meta[@name="author"]/@content').get()
        if not author:
            author = response.xpath('//meta[@property="article:author"]/@content').get()
        if not author:
            author = response.css('span.byline__name::text, a[rel="author"]::text, .author-name::text, .byline a::text').get()
        return self.clean_text(author) or "No Author Found"

    def extract_date(self, response):
        """ Extracts the article date using a fallback chain. """
        date = response.xpath('//meta[@property="article:published_time"]/@content').get()
        if not date:
            date = response.css('time::attr(datetime)').get()
        if not date:
            date = response.xpath('//meta[@name="pubdate"]/@content').get()
        if not date:
             date = response.xpath('//meta[@name="cXenseParse:recs:publishtime"]/@content').get() # For Nasdaq
        if not date:
            date = response.xpath('//meta[@name="date"]/@content').get()
        return self.clean_text(date) or "No Date Found"

    def extract_summary(self, response):
        """ Extracts a summary using a fallback chain. """
        summary = response.xpath('//meta[@property="og:description"]/@content').get()
        if not summary:
            summary = response.xpath('//meta[@name="description"]/@content').get()
        if not summary:
            summary = response.css('div[itemprop="description"]::text').get()

        return self.clean_text(summary) or "No Summary Found"

    def clean_text(self, text):
        """ Remove unwanted characters or whitespace. """
        if not text:
            return ""
        # Consolidate multiple whitespace characters into a single space
        return ' '.join(text.strip().split())