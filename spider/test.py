from typing import Iterable

import scrapy
from scrapy.http.request import Request
from scrapy.http.response import Response
from scrapy.spiders import Spider

class QuotesSpider(scrapy.Spider):
    name = "test"
    start_urls = [
        "https://codeforces.com/problemset/page/1",
    ]

    def start_requests(self) -> Iterable[Request]:
        for url in self.start_urls:
            yield Request(url=url, callback=self.parse)

    def parse(self, res: Response):
        print(f'----------begin {res.url}')
        for li in res.css('table tr')[1:-1]:
            obj =  {
                'id': li.css('td:nth-of-type(1) a::text').get(),
                'url': li.css('td:nth-of-type(1) a::attr("href")').get(),
                'title': li.css('td:nth-of-type(2) a::text').get(),
                'difficulty': li.css('td:nth-of-type(4) span::text').get(),
                'participants': li.css('td:last-child a::text').get(),
            }
            for k in obj.keys():
                try:
                    obj[k] = obj[k].strip()
                except AttributeError as e:
                    pass
            print(obj)
            yield obj
        print('----------end')
        next = res.css('div.pagination li:last-child a::attr("href")').get()
        if next is not None:
            yield res.follow(next, self.parse)