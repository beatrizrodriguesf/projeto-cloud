from bs4 import BeautifulSoup
import requests

def get_day_temp_sp():
    url = "https://g1.globo.com/previsao-do-tempo/sp/sao-paulo.ghtml"

    html = requests.get(url).content
    soup = BeautifulSoup(html, 'html.parser')
    #print(soup.prettify())

    script = soup.find("script", type="application/ld+json")
    script = script.text.strip().split("\n")

    for line in script:
        str = "name"
        if str in line:
            break

    info = line.strip().split(":")
    sp_temp = info[1].strip()
    sp_temp_tratado = sp_temp[1:len(sp_temp)-2]
    return sp_temp_tratado