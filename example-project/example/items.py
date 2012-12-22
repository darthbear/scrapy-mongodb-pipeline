# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field

class Deal(Item):
    MONGODB_COLLECTION = "deals"
    id = Field()
    url = Field()
