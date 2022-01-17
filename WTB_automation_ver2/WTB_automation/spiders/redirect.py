import scrapy
from scrapy.crawler import CrawlerProcess

class redirect(scrapy.Spider):
    handle_httpstatus_list = [302]
    name='redirect'
    start_urls = ["https://track.app.channeliq.com:443/api/wtb/redirect/8597af67-4f2a-4836-b8ae-1ec8fe402ec6/4?rurl=aHR0cDovL2dvLnJlZGlyZWN0aW5nYXQuY29tLz9pZD04MjA1MFgxNTMzNTU5JnhzPTEmdXJsPWh0dHBzJTNBJTJGJTJGd3d3LmNvc3Rjby5jb20lMkZwcmVtaWVyLTMwZy1wcm90ZWluLXNoYWtlcy0xMS1mbC4tb3ouJTI1MmMtMTgtcGFjay5wcm9kdWN0LjEwMDMwODcyNC5odG1sJnhjdXN0PTRjOTQyMmVlYmNmNDhmYWFmNGI3N2U3ZTExNjczZDJm&cpid=00000000-5c09-8328-a1df-aa11f0207e46&mpid=962ce664-0b4e-4a5d-a201-227acf8f60b3&osk=00000000-0000-0000-0000-000000000501&zp=&vs="]

    def _parse(self, response):
        if response.status == [302]:
            yield {
                "r" : response.url
            }


process = CrawlerProcess()
process.crawl(redirect)
process.start()