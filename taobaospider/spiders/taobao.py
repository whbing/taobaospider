# -*- coding: utf-8 -*-

import scrapy
import os
from taobaospider.items import TaobaoItem

#获取分类
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    #为了爬虫稳定，这个url已经保存到本地,start_urls写绝对路径即可
    #如file:///C:/Users/Administrator/Desktop/new/taobao.html
    #网络url为：https://www.taobao.com/
    start_urls = ['file:///'+os.path.abspath('resource/taobao.html')]

    def parse(self, response):
                
        divs = response.xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div/div/div/div[1]/div')

        for div in divs:
                
            item = TaobaoItem()

            item['class1'] = div.xpath('h5/a/text()')[0].extract()
            item['class2'] = div.xpath('p/a/text()').extract()
        
            yield item
    