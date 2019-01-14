# -*- coding: utf-8 -*-
import scrapy
from ..items import MovieItem

class MeijuSpider(scrapy.Spider):
    name = 'meiju'
    allowed_domains = ['meijutt.com']
    start_urls = ['https://www.meijutt.com/new100.html']

    def parse(self, response):
        #获取剧集名
        movie_list=response.xpath('//ul[@class="top-list  fn-clear"]/li')
        for movie in movie_list:
            name = movie.xpath('./h5/a/text()').extract_first()
            print(name)
            item = MovieItem()
            item['name'] = name
            yield item           #相当于同步脚本方法中的return
