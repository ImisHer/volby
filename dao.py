"""
projekt_3.py: třetí projekt

author: Dao Quang Dung
email: daoqu67979@mot.sps-dopravni.cz
discord: Zunz AZA
"""

import sys
sys.argv = [
    "projekt_3.py",
    "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101",
    "vysledky_ceske_budejovice.csv"
]
import requests
from bs4 import BeautifulSoup
import csv


def stahni_html(url):
    response = requests.get(url)
    if response.status_code != 200:
        print("Chyba při stahování stránky")
        sys.exit(1)
    return response.text


def ziskej_odkazy_na_obce(html):
    soup = BeautifulSoup(html, "html.parser")
    odkazy = soup.select("td.cislo a")
    return ["https://volby.cz/pls/ps2017nss/" + a["href"] for a in odkazy]


def zpracuj_obec(url):
    html = stahni_html(url)
    soup = BeautifulSoup(html, "html.parser")


    nadpis = soup.find("h3")
    nazev_obce = nadpis.text.strip() if nadpis else "Neznámá obec"
    
 
    from urllib.parse import urlparse, parse_qs
    qs = parse_qs(urlparse(url).query)
    kod_obce = qs.get("xobec", ["000000"])[0]


    volici = soup.select_one("td[headers=sa2]").text.replace("\xa0", "").strip()
    obalky = soup.select_one("td[headers=sa3]").text.replace("\xa0", "").strip()
    platne_hlasy = soup.select_one("td[headers=sa6]").text.replace("\xa0", "").strip()


    strany = soup.select("td.t1name, td.t2name")
    hlasy = soup.select("td.t1sa2, td.t2sa2")

    vysledky = {
        strany[i].text.strip(): hlasy[i].text.replace("\xa0", "").strip()
        for i in range(len(strany))
    }

    return {
        "kod": kod_obce,
        "nazev": nazev_obce,
        "volici": volici,
        "obalky": obalky,
        "platne_hlasy": platne_hlasy,
        "strany": vysledky
    }


def uloz_csv(jmeno_souboru, vysledky):
    hlavicky = ["kód obce", "název obce", "voliči", "obálky", "platné hlasy"]
    vsechny_strany = sorted(set().union(*(v["strany"].keys() for v in vysledky)))
    hlavicky.extend(vsechny_strany)

    with open(jmeno_souboru, mode="w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(hlavicky)

        for obec in vysledky:
            radek = [
                obec["kod"],
                obec["nazev"],
                obec["volici"],
                obec["obalky"],
                obec["platne_hlasy"]
            ]
            for strana in vsechny_strany:
                radek.append(obec["strany"].get(strana, "0"))
            writer.writerow(radek)


def main():
    if len(sys.argv) != 3:
        print("Zadej správně 2 argumenty: [URL] [vystupní_soubor.csv]")
        sys.exit(1)

    url = sys.argv[1]
    vystup = sys.argv[2]

    print("Stahuji seznam obcí...")
    html = stahni_html(url)
    odkazy_na_obce = ziskej_odkazy_na_obce(html)

    print(f"Nalezeno {len(odkazy_na_obce)} obcí. Zpracovávám...")

    vysledky = []
    for i, obec_url in enumerate(odkazy_na_obce):
        print(f"   ({i+1}/{len(odkazy_na_obce)}) {obec_url}")
        vysledky.append(zpracuj_obec(obec_url))

    print(f"Ukládám do souboru {vystup}")
    uloz_csv(vystup, vysledky)
    print("Hotovo!")


if __name__ == "__main__":
    main()