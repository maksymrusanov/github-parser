import requests
from bs4 import BeautifulSoup

URL = "https://github.com/trending"

HEADERS = {"User-Agent": "Mozilla/5.0"}


def take_info(language: str = None):
    if language:
        response = requests.get(URL + f"/{language.lower()}", headers=HEADERS)
    else:
        response = requests.get(URL, HEADERS)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    repos = []

    for repo in soup.select("article.Box-row"):
        # owner / repo
        full_name = repo.h2.a.get_text(strip=True).replace(" ", "")
        owner, name = full_name.split("/")
        desc = repo.p.get_text(strip=True)

        # language
        lang_tag = repo.select_one('span[itemprop="programmingLanguage"]')
        language = lang_tag.text if lang_tag else "Unknown"

        repos.append(
            {
                "owner": owner,
                "repo": name,
                "url": f"https://github.com/{owner}/{name}",
                "language": language,
                "desc": desc,
            }
        )

    return repos
