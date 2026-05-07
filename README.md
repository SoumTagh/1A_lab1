# 1A_lab_1

## Overview
This lab implements the first step of a data pipeline: Data ingestion. The goal is to scrape GitHub search results for mental health AI repositories and store the extracted data in CSV files for further processing.

### Part 1 - Anatomy of a request
I used the requests library to send an HTTP GET request to GitHub search, defined custom HTTP headers (User-Agent) to mimic a real browser and avoid being blocked, checked the response status code for graceful error handling and saved the raw HTML response to a text file to observe its unstructured nature.

### Part 2 - Static web scraping
I used BeautifulSoup (BS4) to parse the raw HTML, located and extracted the following fields from each repository card (name, url, description, stars and language), stored the extracted data into a Pandas DataFrame and exported it as a CSV file.

### Part 3 - Multi-page scraping
I observed that GitHub pagination changes the url with a &p=X parameter, hardcoded a list of pages to scrape, added time.sleep(2) between requests to avoid rate limiting and combined all results into a single CSV file.
