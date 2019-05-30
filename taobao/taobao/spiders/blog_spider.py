#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-5-30 下午2:48
# @Author : Liuchuan
# @File   : blog_spider.py

from scrapy.spiders import Spider

class BlogSpider(Spider):
    name = 'woodenrobot'
    start_urls = ['http://woodenrobot.me']

    def parse(self, response):
        titles = response.xpath('//a[@class="post-title-link"]/text()').extract()
        for title in titles:
            print(title.strip())
