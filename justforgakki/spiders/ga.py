# -*- coding:utf-8 -*-
from PIL import Image
from scrapy import spider
import requests
from scrapy.selector import Selector
from justforgakki.items import JustforgakkiItem
import re
import urllib2
from scrapy.http import Request
import time


class scr(spider.Spider):
    name = "gakki"                                    #唯一的爬虫名字
        #allowed_domains = ["blu-raydisc.tv"]              #允许的域，防止无限爬

    #allowed_domains = ["pic.sogou.com"]
    num=0
    i=0
    start_urls=["http://pic.sogou.com/pics?query=%D0%C2%D4%AB%BD%E1%D2%C2&mode=1&start=0&reqType=ajax&reqFrom=result&tn=0"]
    '''i=0
    url="http://pic.sogou.com/pics?query=%D0%C2%D4%AB%BD%E1%D2%C2&mode=1&start="+str(i)+"&reqType=ajax&reqFrom=result&tn=0"'''
    custom_settings = {
        'DEFAULT_REQUEST_HEADERS':{'Host':'pic.sogou.com',
       'Connection':'keep-alive',
       'Accept': '*/*',
       'X-Requested-With':'XMLHttpRequest',
       'User-Agent': 'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
       'Referer':'http://pic.sogou.com/pics?sogouexplorer=1&query=%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3&p=59340500',
       'Accept-Language': 'zh-CN,zh;q=0.8',
       }
    }
    image_names={}
    headers ={'Host':'pic.sogou.com',
           'Connection':'keep-alive',
           'Accept': '*/*',
           'X-Requested-With':'XMLHttpRequest',
           'User-Agent': 'Mozilla/5.0 (WindowsNT 6.1; WOW64) AppleWebKit/537.36 '+
           '(KHTML, like Gecko)Chrome/50.0.2661.102 Safari/537.36',
           'Referer':'http://pic.sogou.com/pics?sogouexplorer=1&query=%E6%96%B0%E5%9E%A3%E7%BB%93%E8%A1%A3&p=59340500&start=0'
                     ,
           'Accept-Language': 'zh-CN,zh;q=0.8',
           }


#print items
#print content
    def parse(self, response):
        cur_url="http://pic.sogou.com/pics?query=%D0%C2%D4%AB%BD%E1%D2%C2&mode=1&start="+str(self.i)+"&reqType=ajax&reqFrom=result&tn=0"
        data = None
        req =urllib2.Request(cur_url, data, self.headers)
        item=JustforgakkiItem()
        re_response =urllib2.urlopen(req)
        content =re_response.read()
        #print content
        #pattern=re.compile('pic_url_noredirect\".*?\"(.*?)\"')
        pattern=re.compile('pic_url\".*?\"(.*?)\"')
        items=re.findall(pattern,content)

        item['image_urls']=items
        yield item
        '''for item in items:
        print type(items)
        item['image']=item'''
        '''if self.i%4==0:
            time.sleep(60)'''
        self.i=self.i+48
        cur_url="http://pic.sogou.com/pics?query=%D0%C2%D4%AB%BD%E1%D2%C2&mode=1&start="+str(self.i)+"&reqType=ajax&reqFrom=result&tn=0"
        if self.i<2400:
            yield Request(cur_url,callback=self.parse)






