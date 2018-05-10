# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import csv

class SamsungSpiderPipeline(object):
    def process_item(self, item, spider):
        return item


class SamsungSpiderInfoPipeline(object):
    def open_spider(self, spider):
        self.f = open('samsung.csv', 'w', encoding='utf8', newline='')
        self.head = [u'手机型号', u'价格', u'运行内存', u'电池容量', u'机身颜色', u'前置像素', u'后置像素']
        self.writer = csv.DictWriter(self.f, fieldnames=self.head)
        self.writer.writeheader()

    def close_spider(self, spider):
        self.f.close()

    def process_item(self, item, spider):
        name = item['name']
        price = item['price']
        mem = item['mem']
        eleCap = item['eleCap']
        color = item['color']
        precam = item['precam']
        postcam = item['postcam']
        self.writer.writerow({self.head[0]: name,
                              self.head[1]: price + '元',
                              self.head[2]: mem,
                              self.head[3]: eleCap + 'mAh',
                              self.head[4]: color,
                              self.head[5]: precam,
                              self.head[6]: postcam
                              })
        # print(line)
        return item
