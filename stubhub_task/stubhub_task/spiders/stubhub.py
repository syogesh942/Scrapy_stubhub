import scrapy
import json
from stubhub_task.items import StubhubScraperItem  # Importing the Scrapy Item class for structured data storage

class StubHubEventSpider(scrapy.Spider):
    name = 'stubhub'  # Unique name for the spider

    start_urls = [
        'https://www.stubhub.com/explore?method=getExploreEvents&lat=MjUuNDQ3ODkwMw%3D%3D&lon=LTgwLjQ3OTIxOTY%3D&to=253402300799999&tlcId=2'
    ]  # StubHub API endpoint with event data

    def start_requests(self):
        """Initiates requests to the provided start URLs."""
        for url in self.start_urls:
            yield scrapy.Request(url, callback=self.parse)  # Sending request and assigning response to parse method

    def parse(self, response):
        """Parses the JSON response and extracts event details."""
        data = json.loads(response.text)  # Load response as JSON
        events = data.get('events', [])[:5]  # Extract up to 5 events (ensuring minimum 5)

        event_list = []  # List to store formatted event data

        for event in events:
            item = StubhubScraperItem()  # Create an instance of Scrapy Item
            item['name'] = event.get("name")  # Extract event name
            item['date'] = event.get("formattedDateWithoutYear")  # Extract event date
            item['time'] = event.get("formattedTime")  # Extract event time
            item['venue'] = event.get("venueName")  # Extract venue
            item['location'] = event.get("formattedVenueLocation")  # Extract location
            item['image_url'] = event.get("imageUrl")  # Extract event image URL

            event_list.append({  # Append formatted event data to the list
                "title": item['name'],
                "datetime": f"{item['date']} {item['time']}",
                "location": f"{item['venue']}, {item['location']}",
                "image_link": item['image_url'],
            })

            yield item  # Yields the item to Scrapy's pipeline for further processing

        with open(r"stubhub's events.json", 'w') as json_file:
            json.dump(event_list, json_file, indent=4)
