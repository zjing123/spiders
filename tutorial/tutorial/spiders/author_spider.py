#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-5-30 下午5:23
# @Author : Liuchuan
# @File   : author_spider.py

from scrapy import Request
from scrapy.spiders import Spider


class AuthorSpider(Spider):
    name = 'author'

    start_urls = ['http://quotes.toscrape.com/']

    def parse(self, response):
        for href in response.css('.author + a'):
            yield response.follow(href, callback=self.parse_author)

        for a in response.css('li.next a'):
            yield response.follow(a, callback=self.parse)

    def parse_author(self, response):
        def extract_with_css(query):
            return response.css(query).get(default='').strip()

        yield {
            'name': extract_with_css('h3.author-title::text'),
            'birthdate': extract_with_css('.author-born-date::text'),
            'description': extract_with_css('.author-description::text')
        }


# class AuthorSpider(Spider):
#     name = 'author'
#
#     start_urls = ['http://quotes.toscrape.com/']
#
#     def parse(self, response):
#         # follow links to author pages
#         for href in response.css('.author + a::attr(href)'):
#             yield response.follow(href, self.parse_author)
#
#         # follow pagination links
#         for href in response.css('li.next a::attr(href)'):
#             yield response.follow(href, self.parse)
#
#     def parse_author(self, response):
#         def extract_with_css(query):
#             return response.css(query).get(default='').strip()
#
#         yield {
#             'name': extract_with_css('h3.author-title::text'),
#             'birthdate': extract_with_css('.author-born-date::text'),
#             'bio': extract_with_css('.author-description::text'),
#         }
