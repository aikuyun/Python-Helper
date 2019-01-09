
from ssr.items import SsrItem

import scrapy
# 导入BoosItem


class BossSpiderSpider(scrapy.Spider):

    # 这里是爬虫的名字
    name = 'ssr-spider'

    # 允许的域名
    allowed_domains = ['github.com']

    # 入口url
    start_urls = ['https://github.com/gfw-breaker/ssr-accounts']

    def parse(self, response):

        # 创建对象

        ssr_item = SsrItem()

        ssr_item['ip'] = response.xpath(
            '//*[@id="readme"]/div[2]/article/table/tbody/tr[1]/td[2]/code/text()').extract_first()
        ssr_item['port'] = response.xpath(
            '//*[@id="readme"]/div[2]/article/table/tbody/tr[2]/td[2]/code/text()').extract_first()
        ssr_item['password'] = response.xpath(
            '//*[@id="readme"]/div[2]/article/table/tbody/tr[3]/td[2]/code/text()').extract_first()
        ssr_item['passType'] = response.xpath(
            '//*[@id="readme"]/div[2]/article/table/tbody/tr[4]/td[2]/code/text()').extract_first()
        ssr_item['protocol'] = response.xpath(
            '//*[@id="readme"]/div[2]/article/table/tbody/tr[5]/td[2]/code/text()').extract_first()
        ssr_item['protocol02'] = response.xpath(
            '//*[@id="readme"]/div[2]/article/table/tbody/tr[6]/td[2]/code/text()').extract_first()

        print(ssr_item)

        yield ssr_item

