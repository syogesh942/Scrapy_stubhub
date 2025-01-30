# Scrapy_stubhub

Overview


The StubHubEventSpider is a web scraper created using Scrapy which focuses on extracting event data from the API of StubHub. It pinpoints details such as event names, dates, times, venue locations, and image URLs from the response. This spider will send a request to an API endpoint that has been predetermined and will process the JSON response by extracting the first five events. These events will be stored in instances of StubhubScraperItem; these instances represent the structure of the scraped data.

The spider begins by calling the API and parses the JSON response to extract information on events. This stores relevant info for each event in the fields of StubhubScraperItem and logs the extracted data in structured JSON form, ready for further processing. Pipeline in Scrapy allows handled data to be much more organized and efficient.

The StubhubScraperItem is a blueprint that helps to show the fields (like name datetime venue/location and image URL) that will be taken from each event and kept.
