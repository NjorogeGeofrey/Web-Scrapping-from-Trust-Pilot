import scrapy
from ..items import TrustItem

class ReviewsSpider(scrapy.Spider):
    name = "views"
    allowed_domains = ["www.trustpilot.com"]
    start_urls = ["https://www.trustpilot.com/review/stripe.com?page=1"]
    page_number = 2

    def parse(self, response):
        items = TrustItem()
        links = response.css("div.styles_cardWrapper__LcCPA")

        for link in links:
            items["Name"] = link.css("span.typography_heading-xxs__QKBS8::text").get()
            items["Review"] = link.css("span.typography_body-m__xgxZ_.typography_appearance-subtle__8_H2l::text").get()
            items["Ratings"] = link.css("div.star-rating_starRating__4rrcf img::attr(alt)").get()
            items["Date_Posted"] = link.css("div.typography_body-m__xgxZ_ time::attr(datetime)").get().strip()
            items["Title"] = link.css("div.styles_reviewContent__0Q2Tg h2::text").get()
            items["Content"] = link.css("div.styles_reviewContent__0Q2Tg p::text").get()
            items["Date_of_Experience"] = link.css("p.typography_body-m__xgxZ_::text").extract()[1]
            items["Date_Replied"] = link.css("div.styles_content__Hl2Mi time::attr(datetime)").get(default='NA')
            items["Reply"] = link.css(".styles_message__shHhX::text").get(default='NA')

            yield items
        next_page = f"https://www.trustpilot.com/review/stripe.com?page={ReviewsSpider.page_number}"
        
        if ReviewsSpider.page_number < 609:
            ReviewsSpider.page_number += 1
            yield response.follow(next_page, callback=self.parse)
