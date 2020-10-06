from scrapy.crawler import CrawlerProcess
from scrapy.utils.project import get_project_settings
from ScrapSurfSpot.ScrapSurfSpot.spiders import Spot2
import os


class Scraper:
    def __init__(self):
        settings_file_path = 'ScrapSurfSpot.ScrapSurfSpot.settings'
        os.environ.setdefault('SCRAPY_SETTINGS_MODULE', settings_file_path)
        self.settings = get_project_settings()
        self.process = CrawlerProcess(self.settings)
        self.spider = Spot2.ExampleSpider 

    def run_spider(self):
        self.process.crawl(self.spider)
        self.process.start()  