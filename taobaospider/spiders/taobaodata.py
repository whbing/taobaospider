# -*- coding: utf-8 -*-
import scrapy
from taobaospider.items import TaobaoDataItem
import json
import os

class TaobaodataSpider(scrapy.Spider):
    name = 'taobaodata'
    allowed_domains = ['tmall.com']
    start_urls = []
    headers = {
        "Accept":"*/*",
        "Accept-Encoding":"gzip, deflate, br",
        "Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
        "Connection":"keep-alive",
        "User-Agent":"Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36"
    }
    cookies = {
        "cna" :    "DJjiD8OFH10CAT23lIiTXyFR",
        "isg" :   "Ajo6UT3aNImsLLhhoGXGof8UiGNWYKVBabD3iEQz5k2YN9pxLHsO1QBF8_kU",
        "hng" :   "",
        "cq"  :  "ccp=1",
        "_m_h5_tk" :   "b4af2270d66aadf53c7b835cf6deb2d7_1513766110159",
        "_m_h5_tk_enc" :   "cda6031fda5377214a182fd2f8e31e28",
        "tk_trace"  :  "1",
        "uc1"  :  "cookie14=UoTdeAQ3yq6Z/Q==&lng=zh_CN&cookie16=VT5L2FSpNgq6fDudInPRgavC+Q==&existShop=false&cookie21=VT5L2FSpdeCsOSyjpv/Iyw==&tag=8&cookie15=VT5L2FSpMGV7TQ==&pas=0",
        "uc3"  :  "sg2=UNWuEJ7f9IQoWsDwq0yvzdQTPJvQlZWUXFS8pLI3QPc=&nk2=1CQSIjmyRQE=&id2=W8zJGuZIMl1Q&vt3=F8dBzLbWAqESapdHcSg=&lg2=Vq8l+KCLz3/65A==",
        "tracknick"  :  "\u67AB\u69FF\u9036\u8FE4",
        "_l_g_" :   "Ug==",
        "ck1"  :  "",
        "unb"  :  "852840375",
        "lgc"  :  "\u67AB\u69FF\u9036\u8FE4",
        "cookie1" :   "UUxDLgz+VLBTjH1RbLj0lLsZGnu3xNlcrQ1r8MY7e+w=",
        "login"  :  "true",
        "cookie17" :   "W8zJGuZIMl1Q",
        "cookie2"  :  "1f92a1d4003918d6520389ad15a3b0a8",
        "_nk_" :   "\u67AB\u69FF\u9036\u8FE4",
        "t"  :  "bc11a7b492ae6194a0358b0b61f69d89",
        "uss"  :  "AnJ3MDWIehER6zTadCfmt8bR5kbOzcF+irTXvDlVafx8ilrB2K7NeVuxIzg=",
        "skt"  :  "c91d91e6a8a7354e",
        "_tb_token_"  :  "ebe339dbe1e5e"
    }
    
    def start_requests(self):
        
               
        try:
            #data =  {"class2": ["羽绒服女", "毛呢外套女", "毛衣女", "针织衫女", "棉服女", "连衣裙", "气场外套女装", "风衣女装", "裤子女装", "卫衣女装", "T恤女装", "阔腿裤女装", "衬衫女装", "牛仔裤女装", "半身裙", "大码女装", "时尚套装女", "西装女", "打底衫女", "夹克女", "皮衣女", "皮草女", "妈妈装", "民族舞台女装", "腔调女装", "私服名媛女装", "甜美风女装", "文艺风女装", "街头风女装", "原创女装", "通勤风女装", "婚纱礼服"], "class1": "女装"}
            #data =  {"class2": ["女鞋", "短靴", "切尔西", "长靴", "袜靴", "小白鞋", "运动鞋女", "帆布鞋", "雪地靴", "乐福鞋", "松糕厚底", "玛丽珍鞋", "低跟", "中跟", "高跟", "妈妈鞋", "男鞋", "靴子", "休闲鞋", "雕花布洛克", "板鞋", "帆布鞋", "运动风", "高帮鞋", "豆豆鞋", "乐福鞋", "船鞋", "增高鞋", "正装商务", "户外休闲鞋", "爸爸鞋"], "class1": "鞋靴"}
            data ={"class2": ["毛衣女", "针织衫女", "连衣裙", "风衣女", "裤子女", "卫衣女", "半身裙", "西装女", "打底衫女", "夹克女",  "婚纱礼服"], "class1": "女装"}

            for key in data['class2']:
                print key
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=60&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=120&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=180&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=240&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=300&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=360&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=420&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=480&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=540&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=600&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=660&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=720&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=780&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=840&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=900&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                self.start_urls.append("https://list.tmall.com/search_product.htm?spm=a220m.1000858.0.0.12753ba7yiUUUi&s=960&q="+key+"&sort=d&style=g&from=mallfp..pc_1_searchbutton&type=pc#J_Filter")
                for url in self.start_urls:
                    #yield self.make_requests_from_url(url)
                    yield scrapy.Request(url,cookies=self.cookies,headers=self.headers, meta={'class1':data['class1'],'class2':key})
         
        except Exception,e:
            print '++++++++++ecception+++++++++++)'
            print str(e)
      
            
    def parse(self, response):
        #获取到每一个商品框
        divs = response.xpath('//*[@id="J_ItemList"]/div')
        if divs:
            print '-----------succces-----------'
        else:
            print '+++++++++++failed+++++++++++++'
            
        class1 = response.meta['class1']
        class2 = response.meta['class2']

        for div in divs:

            item = TaobaoDataItem()
            if len(div.xpath('div/div[3]/a/text()'))>0 or len(div.xpath('div/p[2]/a/text()'))>0:
                
                #以下的xpath可能有变动，自己微调
                if len(div.xpath('div/p[2]/a/text()')) > 0 :
                    item['title'] = div.xpath('div/p[2]/a/text()')[0].extract().strip() if len(div.xpath('div/p[2]/a/text()'))>0 else ''
                else:
                    item['title'] = div.xpath('div/div[3]/a/text()')[0].extract().strip() if len(div.xpath('div/div[3]/a/text()'))>0 else ''
                item['price'] = div.xpath('div/p[1]/em/text()')[0].extract().strip() if len(div.xpath('div/p[1]/em/text()'))>0 else ''
                if len(div.xpath('div/p[3]/span[1]/em/text()'))>0:
                    sales_str = div.xpath('div/p[3]/span[1]/em/text()')[0].extract().strip()[:-1] if len(div.xpath('div/p[3]/span[1]/em/text()'))>0 else '-1'
                    item['sales'] = float(sales_str[:-1]) * 10000 if '万'.decode('utf-8') in sales_str else float(sales_str)                   
                else:                    
                    sales_str = div.xpath('div/p[2]/span[1]/em/text()')[0].extract().strip()[:-1] if len(div.xpath('div/p[2]/span[1]/em/text()'))>0 else '-1'
                    item['sales'] = float(sales_str[:-1]) * 10000 if '万'.decode('utf-8') in sales_str else float(sales_str)                   
                if len(div.xpath('div/div[2]/a/text()'))>0:
                    item['store'] = div.xpath('div/div[2]/a/text()')[0].extract().strip() if len(div.xpath('div/div[2]/a/text()'))>0 else ''
                else:
                    item['store'] = div.xpath('div/div[4]/a/text()')[0].extract().strip() if len(div.xpath('div/div[4]/a/text()'))>0 else ''
                    
                item['class1'] = class1 
                item['class2'] = class2 
            
                yield item
    