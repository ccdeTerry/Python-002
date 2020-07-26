# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import pandas

class MaoyanPipeline:
    def process_item(self, item, spider):
        # return item
        name = item['name']
        star = item['star']
        movieType = item['movieType']
        movieList[name,star,movieType]
        moviesRes = pandas.DataFrame(data=movieList)
        print(moviesRes)
        moviesRes .to_csv('./maoyanScrapy.csv',mode='a',encoding='utf8',index=False,header=False)
