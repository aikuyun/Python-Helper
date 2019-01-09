
# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class SsrItem(scrapy.Item):

    # define the fields for your item here like:
    # name = scrapy.Field()
    # 对应我想获取的对象

    ip = scrapy.Field()

    password = scrapy.Field()

    port = scrapy.Field()

    passType = scrapy.Field()

    protocol = scrapy.Field()

    protocol02 = scrapy.Field()
