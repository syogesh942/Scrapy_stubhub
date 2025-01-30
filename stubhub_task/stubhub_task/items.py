# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy  # Import Scrapy module

class StubhubScraperItem(scrapy.Item):
    """Defines the fields for storing scraped event data."""

    name = scrapy.Field()  # Stores the event name
    date = scrapy.Field()  # Stores the event date
    time = scrapy.Field()  # Stores the event time
    venue = scrapy.Field()  # Stores the venue venue
    location = scrapy.Field()  # Stores the location
    image_url = scrapy.Field()  # Stores the URL of the event image