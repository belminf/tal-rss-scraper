#!/usr/bin/env python
from scrapy import signals
from scrapy.settings import CrawlerSettings
from scrapy.crawler import Crawler

from twisted.internet import reactor

from tal.spiders.tal_spider import TALSpider

def main():
    """Setups item signal and run the spider"""

    # set up signal to catch items scraped
    def catch_item(sender, item, **kwargs):
        try:
            print("""\
    <item>
        <title>#{number}: {title}</title>
        <link>{link}</link>
        <description>{description}</description>
        <pubDate>{pubdate}</pubDate>
        <guid>{audio_url}</guid>
        <enclosure url="{audio_url}" length="0" type="audio/mpeg" />
    </item>\
""".format(**item))
        except:
            print 'ERROR', item


    # shut off log
    settings = CrawlerSettings()
    settings.overrides['LOG_ENABLED'] = False

    # set up crawler

    crawler = Crawler(settings)
    crawler.signals.connect(catch_item, signal=signals.item_passed)
    crawler.signals.connect(reactor.stop, signal=signals.spider_closed)
    crawler.configure()

    # schedule spider
    crawler.crawl(TALSpider())

    # print header
    with open('header.xml') as f:
        print f.read()

    # start engine scrapy/twisted
    crawler.start()
    reactor.run()

    # print footer
    with open('footer.xml') as f:
        print f.read()


if __name__ == '__main__':
    main()
