# Volby 2017 – Python projekt

## Autor
- **Jméno:** Dao Quang Dung  
- **Email:** daoqu67979@mot.sps-dopravni.cz  
- **Discord:** Zunz AZA

---

## projektu

Tento Python projekt získává výsledky voleb do Poslanecké sněmovny z roku **2017** ze stránek [volby.cz](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).  
Skript zpracuje data pro **konkrétní okres**, projde všechny obce a uloží výsledky hlasování do `.csv` souboru.

---

## Co program dělá:

- Stáhne HTML stránky pro zvolený okres
- Najde odkazy na všechny obce v okrese
- Pro každou obec získá:
  - kód a název obce
  - počet voličů, obálek, platných hlasů
  - počet hlasů pro každou stranu
- Všechna data uloží do jednoho `.csv` souboru

---

## Jak program spustit

### 1. Instalace potřebných knihoven

Nejdříve nainstalujte knihovny uvedené v souboru `requirements.txt`:
```bash
pip3 install -r requirements.txt

2. Spuštění skriptu
Skript se spouští z terminálu se dvěma argumenty:

bash
Sao chép
Chỉnh sửa
python3 dao.py "ODKAZ_NA_OKRES" "nazev_vystupu.csv"
🧪 Příklad použití
Pro okres České Budějovice (Jihočeský kraj):

Odkaz na okres:
https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=6201

Výstupní soubor:
vysledky_ceske_budejovice.csv

Příkaz pro spuštění:

bash
Sao chép
Chỉnh sửa
python3 dao.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=6201" vysledky_ceske_budejovice.csv
📂 Soubory v projektu
Soubor	Popis
dao.py	Hlavní Python skript
requirements.txt	Seznam knihoven k instalaci
README.md	Tento popis projektu
vysledky_ceske_budejovice.csv	Výstupní soubor s výsledky

✅ Výstupní CSV obsahuje:
Kód obce

Název obce

Počet voličů v seznamu

Vydané obálky

Platné hlasy

Počty hlasů pro jednotlivé strany

📬 Kontakt
Pokud byste měli jakékoliv dotazy, neváhejte mě kontaktovat:

Email: daoqu67979@mot.sps-dopravni.cz

Děkuji za přečtení 🙌
