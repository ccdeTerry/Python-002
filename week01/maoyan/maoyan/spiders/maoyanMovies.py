import scrapy


class MaoyanmoviesSpider(scrapy.Spider):
    name = 'maoyanMovies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

    def parse(self, response):
        # pass

            uri = 
