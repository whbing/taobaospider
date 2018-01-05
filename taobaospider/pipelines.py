# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import codecs
import json

class TaobaospiderPipeline(object):
    def __init__(self):
        #self.file = codecs.open('class.json', 'wb', encoding='utf-8')
        self.file = codecs.open('r1-women-clothing.json', 'wb', encoding='utf-8')
        #self.file = codecs.open('result-1-2-women-clothing.json', 'a+', encoding='utf-8')
             
    def process_item(self, item, spider):
        #如果适用于获取分类的scrapy

        line = json.dumps(dict(item)) + "\n" 
        self.file.write(line.decode('unicode_escape'))
        return item