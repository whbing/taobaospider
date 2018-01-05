# -*- coding: utf-8 -*-

import scrapy
from taobaospider.items import TaobaoItem

#获取分类
class TaobaoSpider(scrapy.Spider):
    name = 'taobao'
    allowed_domains = ['taobao.com']
    start_urls = ['file:///C:/Users/Administrator/Desktop/new/taobao.html']

    def parse(self, response):
        #lis = response.xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div/ul/li/a') 
 
        
        divs = response.xpath('/html/body/div[4]/div[1]/div[1]/div[1]/div/div/div/div[1]/div')

        for div in divs:
                
            item = TaobaoItem()

            item['class1'] = div.xpath('h5/a/text()')[0].extract()
            item['class2'] = div.xpath('p/a/text()').extract()

        
            yield item
    