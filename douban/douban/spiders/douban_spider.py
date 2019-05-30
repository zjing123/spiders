#!/usr/bin/env python3.6
# -*- coding:UTF-8 -*-
# @TIME   : 19-5-30 下午3:02
# @Author : Liuchuan
# @File   : douban_spider.py

from scrapy import Request
from scrapy.spiders import Spider
from douban.items import DoubanItem

class DoubanMovieTop250Spider(Spider):
    name='douban_movie_250'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/53.0.2785.143 Safari/537.36',
    }

    def start_requests(self):
        url = 'https://movie.douban.com/top250'
        yield Request(url, headers=self.headers)

    def parse(self, response):
        item = DoubanItem()
        movies = response.xpath('//ol[@class="grid_view"]/li')
        for movie in movies:
            item['ranking'] = movie.xpath('//div[@class="star"]/span[2]/text()').extract_first()
            item['movie_name'] = movie.xpath('//div[@class="hd"]/a/span[1]/text()').extract_first()
            item['score'] = movie.xpath('//div[@class="star"]/span[2]/text()').extract_first()
            item['score_num'] = movie.xpath('//div[@class="star"]/span[4]').re(r'(\d+)人评价')[0]
            yield item



# <li>
#             <div class="item">
#                 <div class="pic">
#                     <em class="">1</em>
#                     <a href="https://movie.douban.com/subject/1292052/">
#                         <img width="100" alt="肖申克的救赎" src="https://img3.doubanio.com/view/photo/s_ratio_poster/public/p480747492.webp" class="">
#                     </a>
#                 </div>
#                 <div class="info">
#                     <div class="hd">
#                         <a href="https://movie.douban.com/subject/1292052/" class="">
#                             <span class="title">肖申克的救赎</span>
#                                     <span class="title">&nbsp;/&nbsp;The Shawshank Redemption</span>
#                                 <span class="other">&nbsp;/&nbsp;月黑高飞(港)  /  刺激1995(台)</span>
#                         </a>
#
#
#                             <span class="playable">[可播放]</span>
#                     </div>
#                     <div class="bd">
#                         <p class="">
#                             导演: 弗兰克·德拉邦特 Frank Darabont&nbsp;&nbsp;&nbsp;主演: 蒂姆·罗宾斯 Tim Robbins /...<br>
#                             1994&nbsp;/&nbsp;美国&nbsp;/&nbsp;犯罪 剧情
#                         </p>
#
#
#                         <div class="star">
#                                 <span class="rating5-t"></span>
#                                 <span class="rating_num" property="v:average">9.6</span>
#                                 <span property="v:best" content="10.0"></span>
#                                 <span>1436269人评价</span>
#                         </div>
#
#                             <p class="quote">
#                                 <span class="inq">希望让人自由。</span>
#                             </p>
#                     </div>
#                 </div>
#             </div>
#         </li>
