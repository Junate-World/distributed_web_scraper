# Distributed Web Scraper

This project is a distributed web scraper built using **Scrapy** and **Selenium**. It is designed to handle websites with dynamic content (JavaScript-rendered) and allows for scalable scraping of multiple websites.

## Features
- **Scrapy**: A high-level web crawling and scraping framework for static websites.
- **Selenium**: For handling dynamic content that requires JavaScript execution.
- **Multiple Spiders**: Can handle multiple spiders to scrape various websites concurrently.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Junate-World/distributed_web_scraper
   cd distributed_web_scraper

   Create and activate a virtual environment (optional but recommended):

bash

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Install the dependencies:
bash

pip install -r requirements.txt


Install ChromeDriver and WebDriver Manager:

bash

pip install selenium webdriver-manager


Install Scrapy:
bash

pip install scrapy


Usage
Running Spiders
To run a spider (example: js_spider):

bash

scrapy crawl js_spider


To create a new spider:

bash

scrapy genspider spider_name domain.com
Example Spiders
js_spider.py: Handles JavaScript-rendered pages using Selenium.
static_spider.py: Scrapes static content from websites.
Saving Output
The scraped data can be saved to a file:

bash

scrapy crawl js_spider -o output.json

## Documentation
Project Structure
bash

distributed_scraper/
│
├── distributed_scraper/       # Scrapy project files
│   ├── spiders/               # Spider definitions
│   │   ├── js_spider.py       # Spider for JavaScript-rendered pages
│   │   └── static_spider.py   # Spider for static pages
│   ├── __init__.py
│   └── settings.py            # Scrapy settings
├── scrapy.cfg                 # Project configuration file
├── requirements.txt           # Project dependencies
├── README.md                  # Project documentation
└── .gitignore                 # Ignored files
Contributing

## Contributing
Feel free to contribute by submitting a pull request. Issues and suggestions are welcome.
#   d i s t r i b u t e d _ w e b _ s c r a p e r  
 #   d i s t r i b u t e d _ w e b _ s c r a p e r  
 