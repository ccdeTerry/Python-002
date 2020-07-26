import scrapy
# from bs4  import BeautifulSoup 
from  maoyan.items import MaoyanItem
from scrapy.selector  import Selector

class MaoyanmoviesSpider(scrapy.Spider):
    name = 'maoyanMovies'
    allowed_domains = ['maoyan.com']
    start_urls = ['https://maoyan.com/']

    # def parse(self, response):
        # pass
    def  start_requests(self):
            maoyanUri = 'https://maoyan.com/films?showType=3'
            yield scrapy.Request(url=maoyanUri,callback=self.parse,dont_filter=False)

    def parse(self,response):
            movesInfo = Selector(response=response).xpath('//div[@class="movie-item-hover"]')
            item = MaoyanItem()
            for movie in movesInfo[:11]:
                name =movie.xpath('./a/div/div[1]/span[@class="name "]/text()').extract()
                star =movie.xpath('./a/div/div[1]/span[@class="score channel-detail-orange"]/i/text()').extract()
                movieTpye =movie.xpath('./a/div/div[2]/text()').extract()
                item['name'] = name
                item['star'] = star[0]+star[1]
                item['movieTpye'] = movieTpye
                yield item


        # 