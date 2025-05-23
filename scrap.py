import requests
from bs4 import BeautifulSoup

headers = {
    "User-Agent": "Mozilla/5.0"
}

prenoms_garcons = []
prenoms_filles = []

boys_urls = [
    "https://probablyhelpful.com/baby_names/boys250.html",
    "https://probablyhelpful.com/baby_names/boys500.html",
    "https://probablyhelpful.com/baby_names/boys750.html",
    "https://probablyhelpful.com/baby_names/boys1000.html"
]

girls_urls = [
    "https://probablyhelpful.com/baby_names/girls250.html",
    "https://probablyhelpful.com/baby_names/girls500.html",
    "https://probablyhelpful.com/baby_names/girls750.html",
    "https://probablyhelpful.com/baby_names/girls1000.html"
]

for url in boys_urls:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    rows = soup.find_all("tr")[1:]  
    for row in rows:
        cols = row.find_all("td")
        if cols:
            name = cols[0].text.strip()
            prenoms_garcons.append(name)

for url in girls_urls:
    res = requests.get(url, headers=headers)
    soup = BeautifulSoup(res.content, "html.parser")
    rows = soup.find_all("tr")[1:] 
    for row in rows:
        cols = row.find_all("td")
        if cols:
            name = cols[0].text.strip()
            prenoms_filles.append(name)

# Supprimer les doublons et trier
prenoms_garcons = set(prenoms_garcons)
prenoms_filles = set(prenoms_filles)

with open("data/prenoms_garcons.txt", "w") as f:
    for prenom in prenoms_garcons:
        f.write(prenom + "\n")

with open("data/prenoms_filles.txt", "w") as f:
    for prenom in prenoms_filles:
        f.write(prenom + "\n")

print(f"{len(prenoms_garcons)} prénoms garçons et {len(prenoms_filles)} prénoms filles écrits dans les fichiers.")
