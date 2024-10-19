# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class TrustItem(scrapy.Item):
    # define the fields for your item here like:
    Name = scrapy.Field()
    Review = scrapy.Field()
    Ratings = scrapy.Field()
    Date_Posted = scrapy.Field()
    Title = scrapy.Field()
    Content = scrapy.Field()
    Date_of_Experience = scrapy.Field()
    Date_Replied = scrapy.Field()
    Reply = scrapy.Field()
    
