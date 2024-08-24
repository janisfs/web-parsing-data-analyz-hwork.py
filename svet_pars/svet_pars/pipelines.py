# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter


class Svet_parsPipeline:
    def process_item(self, item, spider):
        return item

import csv

class CsvWriterPipeline:
    def __init__(self):
        self.file = open('data.csv', 'w', newline='', encoding='utf-8')
        self.writer = csv.writer(self.file)

    def process_item(self, item, spider):
        self.writer.writerow([item['Название'], item['Цена'], item['Ссылка']])
        return item