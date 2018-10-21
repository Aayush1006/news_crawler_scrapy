# -*- coding: utf-8 -*-
import scrapy
from newscrawler.items import NewscrawlerItem

class Newscrawler1Spider(scrapy.Spider):
    name = 'newscrawler1'
    #allowed_domains = ['theguardian.com/au']
    start_urls = ['http://theguardian.com/au/']

    def parse(self, response):
        for href in response.xpath("//div[contains(@class,'fc-item__container')]/a[contains(@class, 'u-faux-block-link__overlay js-headline-text')]/@href"):
            url =  href.extract()
            yield scrapy.Request(url, callback=self.parse_dir_contents)
            
    def parse_dir_contents(self,response):
        item  = NewscrawlerItem()
##        item['headline'] = response.xpath("//div[contains(@class,'u-cf')]/h1[contains(@class, 'content__headline')]/descendant::text()").extract().strip()
##        item['author'] = response.xpath("//a[contains(@class,'tone-colour')]/span[contains(@itemprop, 'name')]/descendant::text()").extract().strip()
##        item['articleUrl'] = response.xpath("//meta[@property='og:url']/@content").extract().strip()
        item['headline'] = ''.join(s.strip() for s in response.xpath("//div[contains(@class,'u-cf')]/h1[contains(@class, 'content__headline')]/descendant::text()").extract())
        item['author'] = ''.join(s.strip() for s in response.xpath("//a[contains(@class,'tone-colour')]/span[contains(@itemprop, 'name')]/descendant::text()").extract())
        item['articleUrl'] = ''.join(s.strip() for s in response.xpath("//meta[@property='og:url']/@content").extract())
        articleText = response.xpath("//div[contains(@class,'content__article-body')]/descendant::text()").extract()
        articleText = [x.strip() for x in articleText if len(x.strip())>1]
        item['articleText'] = "".join(articleText)
        yield item
    
