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
            for movie in movesInfo[:11]:
                items = MaoyanItem()
                name =movie.xpath('./a/div/div[1]/span[@class="name "]/text()').extract()
                movie_date =movie.xpath('./a/div/div[@class="movie-hover-title movie-hover-brief"]/text()').extract()[1].strip()
                movie_type =movie.xpath('./a/div/div[2]/text()').extract()[1].strip()
                items['name'] = name
                items['movie_date'] = movie_date
                items['movie_type'] = movie_type
                # print(items)
                yield items

        # 