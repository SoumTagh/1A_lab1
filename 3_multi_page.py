import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8",
    "Accept-Language": "en-US,en;q=0.8",
    "Accept-Encoding": "gzip, deflate, sdch",
    "Connection": "keep-alive",
    "Referrer": "https://www.google.com/"
}

# defining the pages i want to scrape
pages = [1, 2, 3, 4, 5]

all_data = []

for page in pages:
    url = f"https://github.com/search?q=mental+health+ai&type=repositories&p={page}"
    
    response = requests.get(url, headers=headers)
    print(f"Page {page} - Status code: {response.status_code}")
    
    # this makes a stop if it gets blocked or hits an error
    if response.status_code != 200:
        print(f"Stopping at page {page} due to status {response.status_code}")
        break

    soup = BeautifulSoup(response.text, "lxml")

    results_container = soup.find("div", attrs={"data-testid": "results-list"})
    
    # skipping if no results found on this page
    if not results_container:
        print(f"No results found on page {page}, skipping...")
        continue

    repo_items = results_container.find_all("div", recursive=False)
    print(f"Page {page} - Repos found: {len(repo_items)}")

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

        all_data.append({
            "name": name,
            "url": repo_url,
            "description": description,
            "stars": stars,
            "language": language
        })

    # waiting 2 seconds between requests to avoid being rate limited
    time.sleep(2)

# saving everything to CSV
df = pd.DataFrame(all_data)
print(f"\nTotal repos scraped: {len(df)}")
print(df)
df.to_csv("github_repos_multipage.csv", index=False)
print("\nData saved to github_repos_multipage.csv")

"""
Page 1 - Status code: 200
Page 1 - Repos found: 10
Page 2 - Status code: 200
Page 2 - Repos found: 10
Page 3 - Status code: 200
Page 3 - Repos found: 10
Page 4 - Status code: 200
Page 4 - Repos found: 10
Page 5 - Status code: 200
Page 5 - Repos found: 10

Total repos scraped: 50
                                                 name  ...          language
0                       kairess/mental-health-chatbot  ...  Jupyter Notebook
1              jahnavik186/AI-Mental-Health-Companion  ...            Python
2                                     PoyBoi/MindEase  ...            Python
3                              Shivam1337/MindCrafter  ...              Dart
4   RCTS-IIITH/AI-Assisted-Mental-Health-Screening...  ...        JavaScript
5                  dhrumilp12/Mental-Health-Companion  ...        JavaScript
6   mujiyantosvc/Facial-Expression-Recognition-FER...  ...            Python
7                     SherazAsghar37/ai_mental_health  ...              Dart
8                                galihru/MentalHealth  ...              HTML
9            Sanjana-Rajagopala/AI_Healthcare_Chatbot  ...              None
10                              ZenYukti/OpenMindWell  ...        TypeScript
11                       VaibhaveS/MentalHealthWithAI  ...            Python
12    arunprasad-04/-Emotion-AI-Mental-Health-Chatbot  ...            Python
13                           neilgebhard/ai-therapist  ...        TypeScript
14              Mercytopsy/AI-Health-Supervisor-Agent  ...  Jupyter Notebook
15                           HemantKumar01/SoulScript  ...        TypeScript
16                                    AryanNayak/Muse  ...  Jupyter Notebook
17                 yogyagit/IvyHacks2024_MentalHealth  ...            Python
18                                    23W-GBAC/RHYAN2  ...            Python
19          Rahul-Sahani04/Mental-Health-AI-Assistant  ...            Python
20              revolutionarybukhari/ai-calling-agent  ...            Python
21                           alvii147/HachikosJournal  ...            Python
22               BinaryStudioAcademy/bsa-2023-calmpal  ...        TypeScript
23                         Sakaar-Sen/MentalHealthBot  ...            Python
24                                   galihru/facemind  ...               TeX
25  siddythings/system-prompts-and-models-of-ai-tools  ...              None
26                  mithatco/mental_health_multiagent  ...            Python
27                          starlightknown/AIry_pages  ...               CSS
28  Saurabhtbj1201/MindSpace-Digital-Mental-Health...  ...        JavaScript
29  SohaibAamir28/Personalized_Mental_Healthcare-C...  ...            Python
30                           behtar-foundation/Sukoon  ...  Jupyter Notebook
31              rrishi0309/Mental-Health-AI-Companion  ...              None
32                aiproduct-creators/mental-health-ai  ...            Python
33          Sukoon-A-Mental-Wellness-Platform/website  ...        JavaScript
34                       shreyasharma04/HealthChatbot  ...            Python
35                              TAHIR0110/ThereForYou  ...            Python
36           Anil951/Early-detection-of-mental-health  ...  Jupyter Notebook
37                                        zenn-ai/zen  ...            Python
38        demoslayer/Mental-health-Chatbot-MERN-STACK  ...        JavaScript
39                  Bhargav1144/Mental_Health_Chatbot  ...            Python
40                     djpapzin/MentalWellnessChatbot  ...            Python
41                                  h8-hackathon/livy  ...        JavaScript
42                                    annu12340/Haven  ...        TypeScript
43                                 Elliot-D-Hill/abcd  ...            Python
44                                Aditya-Ohri/Self.ai  ...              HTML
45  darshitk19/AI-Powered_Mental_Health_Prediction...  ...  Jupyter Notebook
46            amrita-thakur/mental-healthcare-chatbot  ...            Python
47                      miriandres/Happy2Help-chatbot  ...            Python
48                   deepakuy/mindbridge-ai-hackathon  ...            Python
49  Adedolapo-Oguntayo/Basic-Needs-Basic-Rights-Ke...  ...  Jupyter Notebook

[50 rows x 5 columns]

Data saved to github_repos_multipage.csv
"""