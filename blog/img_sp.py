# _*_ coding: utf-8 _*_

#用于爬取bing的每日图片

import urllib2
import re

def GetPage():
    url = 'http://global.bing.com/'
    ua = {
    'User-Agent':'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/48.0.2564.103 Safari/537.36'
    }
    req = urllib2.Request(url,headers=ua)
    response = urllib2.urlopen(req)
    return response.read()

def GetLink(html):
    s_start = html.index("url:'")
    s_end = html.index('jpg')
    return html[s_start + 5 : s_end] + 'jpg'

if __name__ == '__main__':
    print GetLink(GetPage())
