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
