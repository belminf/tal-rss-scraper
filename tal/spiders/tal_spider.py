#!/usr/bin/env python

from __future__ import unicode_literals

from datetime import date
from scrapy.spider import BaseSpider
from scrapy.selector import HtmlXPathSelector

from tal.items import TALEpisode


THIS_YEAR = date.today().year
FIRST_YEAR = 1995
ARCHIVE_URL = 'http://www.thisamericanlife.org/radio-archives/{0}'
EPISODE_URL = 'http://audio.thisamericanlife.org/jomamashouse/ismymamashouse/{0}.mp3'


class TALSpider(BaseSpider):
    name = 'tal'
    start_urls = [ARCHIVE_URL.format(year) for year in range(FIRST_YEAR, THIS_YEAR)]

    def parse(self, response):
        hxs = HtmlXPathSelector(response)
        for e in hxs.select('//div[@id="archive-episodes"]/div/ul/li/div/h3/a/text()'):
            episode_num, episode_name = e.extract().strip().split(': ', 1)
            yield TALEpisode(
                id=episode_num.encode('utf-8'),
                name=episode_name.encode('utf-8'),
                mp3=EPISODE_URL.format(episode_num).encode('utf-8')
            )

