# -*- coding: utf-8 -*-
import scrapy
from quote.items import QuoteItem


class BotQuotesSpider(scrapy.Spider):
    name = "bot_quotes"
    allowed_domains = ["brainyquote.com"]
    start_urls = ['http://brainyquote.com/']

    def parse(self, response):
        html_author = '//div/h2[contains(text(),"opular") and contains(text(),"thors")]/..//div[contains(@class,"bqLn")]'
        for individual_autor in response.xpath (html_author):
            author_name = individual_autor.xpath('./a/text()').extract_first()
            author_link = individual_autor.xpath('./a/@href').extract_first()

            ## Declare information Item for authors
            item = QuoteItem()
            item['author_name'] = author_name
            full_author_url = response.urljoin(author_link)

            yield scrapy.Request(full_author_url, callback=self.parse_author, meta={'item':item})
            break
    ## End parse

    def parse_author(self, response):
        # Extrate the author nationallity 
        author_nationality = response.xpath('//div[contains(@class,"bqLn") and contains(text(), "nality")]/a/text()').extract_first()
        quote_author_path = '//div[contains(@id, "quotesList")]//div[contains(@class,"bqQt")]'
        # quote_list = []

        for individual_quote_author in response.xpath(quote_author_path):
            individual_quote_author_url = individual_quote_author.xpath( './a/img/@src').extract_first()

            # Get the item from the last response
            item = QuoteItem(response.meta['item'])
            item['image_urls'] = []

            # Validate the individual quote url has an image
            if individual_quote_author_url:
                individual_quote_author_url = response.urljoin(individual_quote_author_url)
                item['image_urls'].append(individual_quote_author_url)

            individual_quote_author_path = './/span[contains(@class, "uote") and contains(@class, "ink")]/a[contains(@href,"quotes")]/text()'
            individual_quote_author_text = individual_quote_author.xpath(individual_quote_author_path).extract_first()

            item['author_nationality'] = author_nationality
            item['quote_text']         = individual_quote_author_text

            yield item
            break
#            individual_quote_author_dict = {
#               'quote_image_url': individual_quote_author_url,
#                'quote_text': individual_quote_author_text
#            }
#            quote_list.append(individual_quote_author_dict)

        ## end for loop quote list

    ## End parse author
