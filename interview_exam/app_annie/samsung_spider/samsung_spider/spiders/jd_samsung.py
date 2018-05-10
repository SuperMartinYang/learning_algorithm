# -*- coding: utf-8 -*-
import json
import time
import scrapy
from scrapy.selector import Selector
from scrapy.contrib.spiders import Spider

from ..items import PhoneItem


class JdSamsungSpider(Spider):
    name = 'jd_samsung'
    allowed_domains = ['jd.com', '3.cn']
    start_urls = [
        'http://list.jd.com/list.html?cat=9987,653,655&ev=exbrand_15127&page=1&sort=sort_rank_asc&trans=1&JL=6_0_0#J_main']
    # XPATH for all elements needed
    _x_query = {
        'next_page': '//*[@id="J_topPage"]/a[2]/@href',
        'all_items': '//div/@data-sku',
        'url': 'div/div[@class[p-img]/a/@href]',
        'item_id': '//ul[@class="parameter2 p-parameter-list"]/li[2]/@title',
        'name': 'normalize-space(//div[@class="sku-name"]/text())',
        'name_img': 'normalize-space(//div[@class="sku-name"]/img/following::text())',
        'mem': '//*[@id="detail"]/div[2]/div[2]/div[1]/div[6]/dl/dd[4]/text()',
        'eleCap': '//*[@id="detail"]/div[2]/div[2]/div[1]/div[10]/dl/dd[1]/text()',
        'color': '//*[@id="detail"]/div[2]/div[2]/div[1]/div[2]/dl/dd[1]/text()',
        'precam': '//*[@id="detail"]/div[2]/div[2]/div[1]/div[8]/dl/dd[1]/text()',
        'postcam': '//*[@id="detail"]/div[2]/div[2]/div[1]/div[9]/dl/dd[3]/text()'
    }

    def parse(self, response):
        sel = Selector(response)
        for skuId in sel.xpath(self._x_query['all_items']):
            url = 'http://item.jd.com/' + skuId.extract() + '.html'
            try:
                yield scrapy.Request(url, meta={'skuId': skuId.extract()}, callback=self.parse_phone)
            except:
                print("yield phone page Error")
        # prevent to be blocked
        time.sleep(10)
        next_page = response.xpath(self._x_query['next_page']).extract()[0]
        if next_page != 'javascript:;':
            url = 'https://list.jd.com/' + next_page
            try:
                # print(url)
                yield scrapy.Request(url, callback=self.parse)
            except:
                print("yield next page Error")
        else:
            print("There's no page any more.")

    def parse_phone(self, response):
        # deal with each item (phone) page
        skuId = response.meta['skuId']
        sel = Selector(response)
        phone = PhoneItem()
        # some special phone will has img tag inside of name path
        name_tmp = sel.xpath(self._x_query['name']).extract()[0]
        name_tmp = name_tmp if name_tmp != '' else sel.xpath(self._x_query['name_img']).extract()[0]
        phone['name'] = name_tmp
        # some phone don't have mem
        phone['mem'] = self.get_text(sel, self._x_query['mem'])
        phone['eleCap'] = self.get_text(sel, self._x_query['eleCap'])
        phone['color'] = self.get_text(sel, self._x_query['color'])
        phone['precam'] = self.get_text(sel, self._x_query['precam'])
        phone['postcam'] = self.get_text(sel, self._x_query['postcam'])
        url = 'https://p.3.cn/prices/mgets?callback=&skuIds=J_' + skuId
        yield scrapy.Request(url, meta={'phone': phone}, callback=self.parse_price)

    def get_text(self, sel, x_ptn):
        # special case, set None
        tmp = sel.xpath(x_ptn).extract()
        return 'None' if not tmp else tmp[0]

    def parse_price(self, response):
        # get phone price
        phone = response.meta['phone']
        jsonRes = response.body[2:-4]
        # print(jsonRes)
        jsonRes = json.loads(jsonRes.decode('utf8'))
        phone['price'] = jsonRes['p']
        yield phone
