import requests

# this is the link i'm scraping
url = "https://github.com/search?q=mental+health+ai&type=repositories"

# these are custom headers to mimic a real browser in order to avoid blocking
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Connection": "keep-alive",
    "Referrer": "https://www.google.com/"
}

# sending the HTTP GET request
response = requests.get(url, headers=headers)

# checking the status code
print(f"Status code: {response.status_code}")

# saving the raw HTML to a text file
with open("github_raw.txt", "w", encoding="utf-8") as f:
    f.write(response.text)

print("HTML saved to github_raw.txt")

"""
this is the output that i got : 

Status code: 200 # means that the request has succeeded 
HTML saved to github_raw.txt
"""
