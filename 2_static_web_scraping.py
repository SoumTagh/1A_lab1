import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://github.com/search?q=mental+health+ai&type=repositories"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Connection": "keep-alive",
    "Referrer": "https://www.google.com/"
}

response = requests.get(url, headers=headers)
print(f"Status code: {response.status_code}")

soup = BeautifulSoup(response.text, "lxml")

# this gets the results container
results_container = soup.find("div", attrs={"data-testid": "results-list"})
repo_items = results_container.find_all("div", recursive=False)

print(f"Repos found: {len(repo_items)}")

# extracting data from each repo
data = []

for repo in repo_items:
    # name & url
    link_tag = repo.find("a", class_="prc-Link-Link-9ZwDx")
    if link_tag:
        name = link_tag.get_text(strip=True)
        repo_url = "https://github.com" + link_tag["href"]
    else:
        name, repo_url = None, None

    # description
    desc_tag = repo.find("div", class_=lambda c: c and "Content-module__Content" in c)
    description = desc_tag.get_text(strip=True) if desc_tag else None

    # stars
    stars_tag = repo.find("a", attrs={"aria-label": lambda v: v and "stars" in v})
    stars = stars_tag["aria-label"].replace(" stars", "") if stars_tag else None

    # language
    lang_tag = repo.find("span", attrs={"aria-label": lambda v: v and "language" in v})
    language = lang_tag["aria-label"].replace(" language", "") if lang_tag else None

    data.append({
        "name": name,
        "url": repo_url,
        "description": description,
        "stars": stars,
        "language": language
    })

# saving everything to CSV
df = pd.DataFrame(data)
print(df)
df.to_csv("github_repos.csv", index=False)
print("\nData saved to github_repos.csv")

"""
this is the output that i got :

Status code: 200
Repos found: 10
                                                name  ...          language
0                      kairess/mental-health-chatbot  ...  Jupyter Notebook
1             jahnavik186/AI-Mental-Health-Companion  ...            Python
2                                    PoyBoi/MindEase  ...            Python
3                             Shivam1337/MindCrafter  ...              Dart
4  RCTS-IIITH/AI-Assisted-Mental-Health-Screening...  ...        JavaScript
5                 dhrumilp12/Mental-Health-Companion  ...        JavaScript
6  mujiyantosvc/Facial-Expression-Recognition-FER...  ...            Python
7                    SherazAsghar37/ai_mental_health  ...              Dart
8                               galihru/MentalHealth  ...              HTML
9           Sanjana-Rajagopala/AI_Healthcare_Chatbot  ...              None

[10 rows x 5 columns]

Data saved to github_repos.csv
"""