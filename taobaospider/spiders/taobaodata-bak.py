# -*- coding: utf-8 -*-
import scrapy
from taobaospider.items import TaobaoDataItem
import json
import os

class TaobaodataSpider(scrapy.Spider):
    name = 'taobaodata'
    allowed_domains = ['taobao.com']
    #start_urls = ['https://list.tmall.com/search_product.htm?q=%C4%D0%D7%B0']
    start_urls = []
    headers = {
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    cookies = {
        'cna' : 'DJjiD8OFH10CAT23lIiTXyFR',
        'isg' : 'Ap2dqCWTmwZ4e38oG9SZuKR1r3pXEtB8gjHwAV9i2fQjFr1IJwrh3GuENDDv',
        'hng' : '', 
        'uss' : 'UUAKKOPPTZ8wa8xT0rhCXH7F7fNV+OG60ivBpF87v8rBxAbu0wgAFY32W7s=',
        'mbk' : 'f0215bed61fd3a9c',
        't'   : 'bc11a7b492ae6194a0358b0b61f69d89',
        'uc3' : 'sg2=UNWuEJ7f9IQoWsDwq0yvzdQTPJvQlZWUXFS8pLI3QPc=&nk2=1CQSIjmyRQE=&id2=W8zJGuZIMl1Q&vt3=F8dBzLbQLjYC8HgzC4U=&lg2=UIHiLt3xD8xYTw==',
        'tracknick': '\u67AB\u69FF\u9036\u8FE4',
        'lgc' : '\u67AB\u69FF\u9036\u8FE4',
        '_tb_token_' : '783a8b8f3efee',
        'cookie2' : '2bc70e326650fc136940b9bb39d385b7',
        '_m_h5_tk':  'b4af2270d66aadf53c7b835cf6deb2d7_1513766110159',
        '_m_h5_tk_enc' : 'cda6031fda5377214a182fd2f8e31e28',
        'uc1' :  'cookie14=UoTdeApSmDmp4w==&lng=zh_CN&cookie16=VFC/uZ9az08KUQ56dCrZDlbNdA==&existShop=false&cookie21=UIHiLt3xSifiVqTH8o/0Qw==&tag=8&cookie15=VFC/uZ9ayeYq2g==&pas=0',
        '_l_g_' : 'Ug==',
        'ck1' : '',  
        'unb' :  '852840375',
        'cookie1' : 'UUxDLgz+VLBTjH1RbLj0lLsZGnu3xNlcrQ1r8MY7e+w=',
        'login' : 'true',
        'cookie17' : 'W8zJGuZIMl1Q',
        '_nk_' : '\u67AB\u69FF\u9036\u8FE4',
        'skt' : '3fe5644fe1b0314b'
    }
    
    def start_requests(self):
        
               
        try:
            data =  open(r'D:\javaTools\EclipseWork1\taobaospider\class.json','r')
            print '=================='
            
            for line in data.readlines():
                dic = json.loads(line)            
                print('class1:')
                print(dic['class1'])
                print 'class2'
                for key in dic['class2']:
                    self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=60&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                    for url in self.start_urls:
                        #yield self.make_requests_from_url(url)
                        yield scrapy.Request(url,cookies=self.cookies,headers=self.headers, meta={'class1':dic['class1'],'class2':key})

         
        except Exception,e:
            print '++++++++++ecception+++++++++++)'
            print str(e)

            
        '''    
        keys= ["男装","女装"]
        for key in keys:
            self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=60&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
        #url = 'https://list.tmall.com/search_product.htm?spm=a220m.1000858.1000724.4.3b676fbc3a7O7o&q=女装&sort=d&style=g&from=.list.pc_1_searchbutton#J_Filter'
        for url in self.start_urls:
            #yield self.make_requests_from_url(url)
            yield scrapy.Request(url)
        '''
    def parse(self, response):
        #获取到每一个框框
        divs = response.xpath('//*[@id="J_ItemList"]/div')
        if divs:
            print '-----------succces-----'
        else:
            print '+++++++++++failed+++++'
            
        class1 = response.meta['class1']
        class2 = response.meta['class2']
        
        for div in divs:

            item = TaobaoDataItem()
            if len(div.xpath('div/p[2]/a/text()'))>0:
                item['title'] = div.xpath('div/p[2]/a/text()')[0].extract().strip() if len(div.xpath('div/p[2]/a/text()'))>0 else 'null'
                item['price'] = div.xpath('div/p[1]/em/text()')[0].extract().strip() if len(div.xpath('div/p[1]/em/text()'))>0 else 'null'
                item['sales'] = div.xpath('div/p[3]/span[1]/em/text()')[0].extract().strip() if len(div.xpath('div/p[3]/span[1]/em/text()'))>0 else 'null'
                item['store'] = div.xpath('div/div[3]/a/text()')[0].extract().strip() if len(div.xpath('div/div[3]/a/text()'))>0 else 'null'
                item['class1'] = class1 
                item['class2'] = class2 
                
    
        
                yield item
    