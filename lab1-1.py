import requests

url = "https://github.com/search?q=mental+health+ai&type=repositories"

# defining http headers
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.9',
    'Accept-Encoding': 'gzip, deflate, br',
    'Connection': 'keep-alive'
}

try:
    response = requests.get(url, headers=headers, timeout=10)
    response.raise_for_status()
    with open("website_content.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
        
    print(f"Successfully saved content from {url}")

except requests.exceptions.HTTPError as err:
    print(f"HTTP error occurred: {err}")
except Exception as err:
    print(f"An error occurred: {err}")

# Sending a GET request to the URL
response = requests.get(url)
# Checking if the request was successful
if response.status_code == 200:
    # Opening a file in 'write' mode and specifying encoding
    with open("output.txt", "w", encoding="utf-8") as file:
        file.write(response.text)
    print("Success! Content written to output.txt")
else:
    print(f"Failed to retrieve content. Status code: {response.status_code}")

