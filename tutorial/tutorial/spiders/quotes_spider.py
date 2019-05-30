#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-5-30 下午4:39
# @Author : Liuchuan
# @File   : quotes_spider.py

from scrapy import Request
from scrapy.spiders import Spider


class QuotesSpider(Spider):
    name = 'quotes'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        urls = [
            'http://quotes.toscrape.com/page/1/',
            'http://quotes.toscrape.com/page/2/',
        ]
        for url in urls:
            yield Request(url=url, headers=self.headers, callback = self.parse)

    def parse(self, response):
        quotes = response.xpath('//div[@class="quote"]')
        for quote in quotes:
            yield self.parse_xpath(quote)

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)

        # for href in response.css('li.next a::attr(href)'):
        #     yield response.follow(href, callback=self.parse)

        # next_page = response.css('li.next a::attr(href)').get()
        # if next_page is not None:
        #     next_page = response.urljoin(next_page)
        #     yield response.follow(next_page, callback=self.parse)


    def parse_xpath(self, quote):
        return {
                'text': quote.xpath('.//span[@class="text"]/text()').extract_first(),
                'author': quote.xpath('.//small[@class="author"]/text()').get(),
                'tags': quote.xpath('.//div[@class="tags"]/a[@class="tag"]/text()').getall()
            }

    def parse_css(self, quote):
        return {
                'text': quote.css('span.text::text').get(),
                'author': quote.css('small.author::text').get(),
                'tags': quote.css('div.tags a.tag::text').getall(),
            }
