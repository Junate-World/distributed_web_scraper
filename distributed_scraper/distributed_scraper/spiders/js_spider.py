import scrapy
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from scrapy.selector import Selector

class JsSpider(scrapy.Spider):
    name = 'js_spider'

    def __init__(self):
        # Initialize Selenium WebDriver with Chrome
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

    def start_requests(self):
        # Replace with the URL you want to scrape
        url = 'https://example.com'  # Change this to your target URL
        self.driver.get(url)

        try:
            # Wait until a specific element is loaded (adjust the selector as needed)
            WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CSS_SELECTOR, 'h1'))  # Adjust selector based on your target page
            )
        except Exception as e:
            self.logger.error(f"Error waiting for element: {e}")

        # Get the fully rendered page source
        page_source = self.driver.page_source

        # Use Scrapy's Selector to process the page after JavaScript has run
        sel = Selector(text=page_source)

        # Pass the page source to Scrapy's parse method
        yield scrapy.Request(url=url, callback=self.parse, meta={'sel': sel})

    def parse(self, response):
        # Extract data using Scrapy's response selector (Selector stored in meta)
        sel = response.meta['sel']

        # Example: Scrape the titles of all articles on the page
        titles = sel.css('h1::text').getall()

        for title in titles:
            # Yield each title as an item
            yield {'title': title}

        # Close the Selenium driver when done
        self.driver.quit()
