import scrapy

class FacultySpider(scrapy.Spider):
    name = "faculty"
    start_urls = ["https://abu.edu.ng/faculties/"]
    
    def parse(self, response):
        faculties = response.css("div.uael-infobox-title-wrap")
        for faculty in faculties:
            yield {
                "faculty": faculty.css("h3::text").get()
            }
