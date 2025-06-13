<!DOCTYPE html>
<html lang="cs">
<head>
  <meta charset="UTF-8" />
</head>
<body>

<h1>Volby 2017 – Python projekt</h1>

<h2>Autor</h2>
<ul>
  <li><strong>Jméno:</strong> Dao Quang Dung</li>
  <li><strong>Email:</strong> daoqu67979@mot.sps-dopravni.cz</li>
  <li><strong>Discord:</strong> Zunz AZA</li>
</ul>

<hr/>

<h2> projektu </h2>
<p>
Tento Python projekt získává výsledky voleb do Poslanecké sněmovny z roku <strong>2017</strong> ze stránek
<a href="https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ" target="_blank">volby.cz</a>.
</p>
<p>
Skript zpracuje data pro zvolený okres, projde všechny obce a uloží výsledky hlasování do souboru <code>.csv</code>.
</p>

<hr/>

<h2> Co program dělá</h2>
<ul>
  <li>Stáhne HTML stránky pro zvolený okres</li>
  <li>Najde odkazy na všechny obce</li>
  <li>Získá pro každou obec:
    <ul>
      <li>kód a název obce</li>
      <li>počet voličů, obálek, platných hlasů</li>
      <li>počet hlasů pro každou stranu</li>
    </ul>
  </li>
  <li>Uloží vše do souboru <code>.csv</code></li>
</ul>

<hr/>

<h2> Jak program spustit</h2>

<h3>1. Instalace knihoven</h3>
<p>
Před spuštěním nainstalujte knihovny pomocí:
</p>
<pre><code>pip3 install -r requirements.txt</code></pre>

<h3>2. Spuštění skriptu</h3>
<p>
Skript se spouští z terminálu se dvěma argumenty:
</p>
<pre><code>python3 dao.py "ODKAZ_NA_OKRES" "nazev_vystupu.csv"</code></pre>

<hr/>

<h2>Příklad použití – okres České Budějovice</h2>
<ul>
  <li>
    <strong>Odkaz:</strong>
    <a href="https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101">
     https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101
    </a>
  </li>
  <li><strong>Název výstupního souboru:</strong> vysledky_ceske_budejovice.csv</li>
  <li>
    <strong>Příkaz pro spuštění:</strong>
    <pre><code>
python3 dao.py "https://www.volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=3&xnumnuts=3101" vysledky_ceske_budejovice.csv
    </code></pre>
  </li>
</ul>

<hr/>

<h2>📂 Soubory v projektu</h2>
<table border="1" cellspacing="0" cellpadding="4">
  <thead>
    <tr>
      <th>Soubor</th>
      <th>Popis</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><code>dao.py</code></td>
      <td>Hlavní Python skript</td>
    </tr>
    <tr>
      <td><code>requirements.txt</code></td>
      <td>Seznam knihoven k instalaci</td>
    </tr>
    <tr>
      <td><code>README.md</code></td>
      <td>Tento popis projektu</td>
    </tr>
    <tr>
      <td><code>vysledky_ceske_budejovice.csv</code></td>
      <td>Výstupní soubor s výsledky</td>
    </tr>
  </tbody>
</table>

<hr/>

<h2> Výstupní CSV obsahuje:</h2>
<ul>
  <li>Kód obce</li>
  <li>Název obce</li>
  <li>Počet voličů v seznamu</li>
  <li>Vydané obálky</li>
  <li>Platné hlasy</li>
  <li>Hlasy pro jednotlivé strany</li>
</ul>

<hr/>

<h2> Kontakt</h2>
<p>
Pokud byste měli jakékoliv dotazy, neváhejte mě kontaktovat:
</p>
<ul>
  <li><strong>Email:</strong> daoqu67979@mot.sps-dopravni.cz</li>
</ul>

<p>Děkuji za přečtení! :)))</p>

</body>
</html>

