import scrapy


class QuotesSpiderSpider(scrapy.Spider):
    name = "quotes_spider"
    start_urls = ["https://quotes.toscrape.com"]

    def parse(self, response):
        for quote in response.css("div.quote"):
            yield {
                "quote": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
            }

            # Follow the next page link
            next_page = response.css("li.next a::attr(href)").get()
            if next_page is not None:
                yield response.follow(next_page, callback=self.parse)
