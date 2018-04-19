#common

CATEGORY_PAGE = 'CATEGORY_PAGE'
SUB_CATEGORY_PAGE='SUB_CATEGORY_PAGE'
PDP_LIST_PAGE='PDP_LIST_PAGE'
PDP_PAGE = 'PDP_PAGE'
PAGINATED_LIST = 'PAGINATED_LIST'

#urls

SOURCE      = 'hnmde'

URL         = 'http://www.hm.com/de/'

CATEGORIES_GENDER_XPATHS  = [
                                {
                                    "GENDER": "WOMEN",
                                    "CATEGORY": "WOMENSWEAR",
                                    "URL": "http://www.hm.com/de/department/LADIES"
                                }, {
                                    "GENDER": "MEN",
                                    "CATEGORY": "MENSWEAR",
                                    "URL": "http://www.hm.com/de/department/MEN"
                                }
                            ]

PAGE_SIZE = 100

'''
PRODUCT_BLOCK_XPATH = ".//main/ul[@class='prod-grid']/li"

PRODUCT_URL_INSIDE_BLOCK_XPATH = ".//a[@class='prod-tile__link']/@href"

CATEGORY_XPATH = ".//div[@class='upper-breadcrumb']/div/a[last()]/text()"

BRAND_XPATH = ".//a[@class='prod-info__brand-link']/text()"

ARTICLETYPE_XPATH = ".//*[@id='top']/section/ul/li[last()-1]/a/span/text()"

CURRENCY_XPATH = ".//meta[@itemprop='priceCurrency']/@content"

ITEM_COUNT_XPATH = ".//div[@id='primary-content']/div[@class='product-grid__col--major']//div/@data-result-total"

PAGE_COUNT_XPATH = ".//select/@data-totalpagecount"

STYLENAME_XPATH = ".//h1[@class='prod-info__name' or @itemprop='name']/text()"

DEFAULTIMAGE_XPATH = ".//meta[@property='og:image']/@content"

IMAGEURLLIST_XPATH = ".//*[@id='prod-slider-thumbnails']/li/img/@data-src"

DESCRIPTION_XPATH= ".//div[@itemprop='description']//text()"

COLOUR_XPATH = ".//div/span[@class='prod-info__color-header__color']/text()"

GENDER_XPATH = ".//div[@class='upper-breadcrumb']/div/a[1]/text()"

SIZES_XPATH = ".//*[@id='selectsize']/option/text()"

SELLING_PRICE_XPATH = ".//meta[@itemprop='price']/@content"

MRP_XPATH = ".//span[@class='prod-info__price-old']/text()"

STYLEID_XPATH = ".//*[@id='selectsize']/@data-group-sku"
 

'''