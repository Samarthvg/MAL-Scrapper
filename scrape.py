import requests
import bs4
import re

res = requests.get('https://myanimelist.net/anime/30/Neon_Genesis_Evangelion/reviews')

soup = bs4.BeautifulSoup(res.text, 'html.parser' )

borderDark = soup.find_all('div', "borderDark")

outputFile = open('output.txt', 'w', encoding="utf-8")

for newSoup in borderDark:

    removeHelpful = newSoup.find_all('a', "button_form")
    removeReadmore = newSoup.find_all('a', "js-toggle-review-button")
    profile = newSoup.find_all('a', href=re.compile("https://myanimelist.net/profile/"))
    reviews = newSoup.find_all('div', "spaceit textReadability word-break pt8 mt8")
    
    for helpful,readmore in zip(removeHelpful, removeReadmore):
        helpful.decompose()
        readmore.decompose()
    for a in profile:
        print(a.get_text("|", strip=True), file = outputFile)
    for div in reviews:
        print(div.get_text("|", strip=True), file = outputFile)

outputFile.close()
