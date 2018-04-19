from selenium import webdriver
from scrapy.http import HtmlResponse
import inspect,sys,time

def getScrapyResponse(url):
    try:
        #print(url)
        driver = webdriver.PhantomJS()
        #print(driver)
        driver.get(url)
        response_html = driver.page_source
        #print(response_html)
        response_html = HtmlResponse(url=url, body=response_html, encoding='utf-8')
        driver.close()
        return response_html
    except:
        e_msg = 'EXCEPTION OCCURRED IN :' + inspect.stack()[0][3]
        e_msg = e_msg + str(sys.exc_info())
        e_msg = e_msg + ' | ' + ' Error on line {}'.format(sys.exc_info()[-1].tb_lineno)
        #print(e_msg)
        pass
    return ''

#print(getScrapyResponse('https://www.lefties.com/sa/women/jeans/super-skinny-ripped-jeans-c1029515p500757003.html'))

