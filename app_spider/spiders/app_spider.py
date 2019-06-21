# -*- coding: utf-8 -*-

"""
File: app_spider.py
Author: jackdan
Date: 2019/06/20 15:50
Description: Crawl the required information from the mobile app.
"""

from __future__ import unicode_literals

import logging
import sys

import scrapy
from scrapy.http import Request

import json
# import requests
from bs4 import BeautifulSoup
import js2xml
from lxml import etree

defaultencoding = 'utf-8'
if sys.getdefaultencoding() != defaultencoding:
    reload(sys)
    sys.setdefaultencoding(defaultencoding)

LOG = logging.getLogger(__name__)


class AppSpider(scrapy.Spider):
    """
    Extract the video link in the shared vibrato video url link
    """

    name = "app"
    start_urls = [
        "http://v.douyin.com/rKJFCv/",
    ]

    def parse(self, response):
        """
        :param response:
        :description: main content
        :return:
        """
        resp = response.text
        soup = BeautifulSoup(resp, 'lxml')
        src = soup.select('body script')[2].string
        src_text = js2xml.parse(src, debug=False)
        src_tree = js2xml.pretty_print(src_text)

        """
        Convert the tags in the `script` to `xml`
        """
        selector = etree.HTML(src_tree)

        """
        Get the elements in the converted `xml` tag
        """
        _item_id = selector.xpath("//property[@name='itemId']/string/text()")[0]
        _dytk = selector.xpath("//property[@name='dytk']/string/text()")[0]
        _center_url = 'https://www.iesdouyin.com/web/api/v2/aweme/iteminfo/?item_ids=' + _item_id + '&dytk=' + _dytk

        yield Request(
            url=_center_url,
            callback=self.parse_content
        )

    def parse_content(self, response):
        json_content = json.loads(response.text)
        video_url = json_content['item_list'][0]['video']['play_addr']['url_list'][0]
        print('###### Source Uri Address ######')
        print(video_url)
        print('###### Source Uri Address ######')

