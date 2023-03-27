import scrapy
from docx import Document

doc = Document()

class GfgArticleSpider(scrapy.Spider):
    name = 'gfg_article'
    allowed_domains = ['www.geeksforgeeks.org']
    start_urls = ['https://www.geeksforgeeks.org/data-structures/?ref=shm']

    def parse(self, response):
        
        title = response.css("h1.entry-title::text").get()
        page_content = response.css('div.page_content *::text').getall()


