import json
import requests
from bs4 import BeautifulSoup

USERNAME = "abhinav28ai"

url = f"https://github.com/users/{USERNAME}/contributions"

html = requests.get(url).text

soup = BeautifulSoup(html, "html.parser")

days = []

# GitHub now stores contributions in td elements
for td in soup.select("td.ContributionCalendar-day"):
    days.append({
        "date": td.get("data-date"),
        "count": int(td.get("data-count", 0)),
        "level": int(td.get("data-level", 0))
    })

print("Found:", len(days), "days")

with open("data/contributions.json", "w") as f:
    json.dump(days, f, indent=2)