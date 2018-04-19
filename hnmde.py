# -*- coding: utf-8 -*-
import scrapy, datetime
import util as util_obj
import hnmde_config as conf
import requests

class HnmdeSpider(scrapy.Spider):
    debug = True
    name = "hnmde"
    allowed_domains = ["hm.com"]
    start_urls      = ['http://www.hm.com/de']
    base_url        =   'http://www.hm.com'

    def parse(self, response):
        page_size = 60
        for category in conf.CATEGORIES_GENDER_XPATHS:
            url = category['URL']
            response = util_obj.getScrapyResponse(url)
            categoryLinks = response.xpath(".//a[contains(@class,'product-link')]/@href").extract()
            if self.debug:
                categoryLinks = categoryLinks[:2]
            for categorylink in categoryLinks:
                if 'www' in categorylink and 'http' not in categorylink:
                    categorylink =  'http:'+categorylink
                if 'http' not in categorylink:
                    categorylink = self.base_url+categorylink

                url_slug = "/".join(categorylink.split('/')[-2:])
                pdpCategory = categorylink.split('/')[-1]
                if self.debug:
                    print(categorylink)
                    print(category['GENDER'])
                    print(url_slug)
                    print(pdpCategory)

                url = "http://api.hm.com/v2/DE/de/products/display?categories=" + url_slug + "&concealCategories=true&pageSize=60&page=1&deviceType=DESKTOP"
                resp = requests.get(url).json()
                input_rank = 1
                if 'pagination' in resp:
                    if 'count' in resp['pagination']:
                        if resp['pagination']['count']>0:
                            product_count = resp['pagination']['count']
                            print(product_count)
                            page_count = (product_count/page_size)+2
                            print(page_count)
                            for i in range(1, page_count):
                                url = "http://api.hm.com/v2/DE/de/products/display?categories="+url_slug+"&concealCategories=true&pageSize="+str(page_size)+"&page="+str(i)+"&deviceType=MOBILE"
                                print(url)
                                resp = requests.get(url).json()
                                for productItem in resp['displayArticles']:

                                    print(productItem)

                                    fdi = {} # FashionDbItem()

                                    fdi['paginatedUrl'] = url

                                    fdi['gender'] = category['GENDER']

                                    fdi['rank'] = input_rank

                                    fdi['source'] = self.name

                                    fdi['run_date'] = str(datetime.datetime.now()).split()[0]

                                    try:
                                        fdi['url'] = productItem['webUrl']
                                    except:
                                        fdi['url'] = ''
                                        pass

                                    try:
                                        fdi['brand'] = 'h & m'
                                    except:
                                        fdi['brand'] = ''
                                        pass

                                    try:
                                        fdi['currency'] = productItem['priceInfo']['currencyIso']
                                    except:
                                        fdi['currency'] = ''  # 'GBP'
                                        pass

                                    try:
                                        fdi['category'] = pdpCategory
                                    except:
                                        fdi['category'] = ""
                                        pass

                                    try:
                                        fdi['articleType'] = pdpCategory
                                    except:
                                        fdi['articleType'] = ''
                                        pass

                                    try:
                                        fdi['styleName'] = productItem['name']
                                    except:
                                        fdi['styleName'] = ''
                                        pass

                                    try:
                                        fdi['defaultImage'] = 'http:'+productItem['primaryImage']['url']
                                    except:
                                        fdi['defaultImage'] = ''
                                        pass

                                    try:
                                        imgLis = []
                                        imgLis.append(fdi['defaultImage'])
                                        imgLis.append('http:'+productItem['secondaryImage']['url'])
                                        fdi['imageUrlList'] = imgLis
                                    except:
                                        fdi['imageUrlList'] = ''
                                        pass

                                    try:
                                        fdi['description'] = ''
                                    except:
                                        fdi['description'] = ''
                                        pass

                                    try:
                                        fdi['colour'] = productItem['colourDescription']
                                    except:
                                        fdi['colour'] = ''
                                        pass

                                    try:
                                        lis = []
                                        for size in productItem['availableSizeInfo']:
                                            lis.append(size['sizeName'])

                                        fdi['sizes'] = lis
                                    except:
                                        fdi['sizes'] = []
                                        pass

                                    try:
                                        fdi['selling_price'] = productItem['priceInfo']['price']
                                    except:
                                        fdi['selling_price'] = ''
                                        pass

                                    try:
                                        fdi['mrp'] = productItem['priceInfo']['price']
                                    except:
                                        fdi['mrp'] = ''
                                        pass

                                    try:
                                        fdi['styleId'] = productItem['articleCode']
                                    except:
                                        fdi['styleId'] = ''
                                        pass

                                    print(fdi)

                                    input_rank = input_rank+1

                                    print("=" * 120)


                                    yield fdi


                        else:
                            print('O Records')


