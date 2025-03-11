# Hydrauliikkajärjestelmän koneoppimisvalvonnan vaatimusmäärittely

## 1. Johdanto
Tämä dokumentti määrittelee vaatimukset hydrauliikkajärjestelmän koneoppimispohjaiselle valvontajärjestelmälle, joka tunnistaa normaalitilat ja vikatilanteet.

## 2. Toiminnalliset vaatimukset

### 2.1 Tilojen tunnistaminen
- Järjestelmän tulee tunnistaa seuraavat tilat:
  - Normaalitilat: normal_operating, normal_highload, normal_lowload
  - Vikatilat: overload, hose_break

### 2.2 Reaaliaikainen valvonta
- Järjestelmän tulee valvoa hydrauliikkajärjestelmän tilaa reaaliajassa
- Näytteenottotaajuus: vähintään 10 Hz
- Vikatilanteiden tunnistusviive: enintään 500 ms

### 2.3 Hälytykset
- Järjestelmän tulee antaa hälytys, kun vikatila tunnistetaan
- Hälytyksen tulee sisältää vikatilan tyyppi ja vakavuusaste
- Kriittiset hälytykset tulee välittää käyttäjälle välittömästi

## 3. Suorituskykyvaatimukset

### 3.1 Tarkkuus
- Luokittelutarkkuus: vähintään 99%
- Väärät positiiviset: enintään 0.1%
- Väärät negatiiviset: enintään 0.1%

### 3.2 Vasteaika
- Ennustuksen laskenta-aika: enintään 50 ms
- Järjestelmän kokonaisviive: enintään 100 ms

### 3.3 Resurssien käyttö
- Muistinkäyttö: enintään 50 MB
- Prosessorikuorma: enintään 10% yhden ytimen suorituskyvystä

## 4. Laitteistovaatimukset

### 4.1 Sulautettu järjestelmä
- Prosessori: vähintään ARM Cortex-M4 (tai vastaava)
- Muisti: vähintään 128 MB RAM
- Tallennustila: vähintään 1 GB

### 4.2 Anturit
- Paineanturi: tarkkuus ±1%, näytteenottotaajuus 100 Hz
- Pumpun ohjaussignaali: tarkkuus ±0.5%, näytteenottotaajuus 100 Hz

## 5. Ohjelmistovaatimukset

### 5.1 Käyttöjärjestelmä
- Reaaliaikainen käyttöjärjestelmä (RTOS) tai baremetal-toteutus

### 5.2 Kirjastot
- Optimoitu koneoppimiskirjasto sulautetulle järjestelmälle
- Tuki SVM-mallille ja MinMaxScaler-komponentille

## 6. Testausvaatimukset

### 6.1 Yksikkötestit
- Kattavuus: vähintään 90% koodista
- Automaattinen testien suoritus CI/CD-putkessa

### 6.2 Järjestelmätestit
- Testaus todellisella hydrauliikkajärjestelmällä
- Kaikkien vikatilanteiden simulointi ja tunnistaminen

## 7. Dokumentaatiovaatimukset
- Koodin dokumentointi: kaikki funktiot ja luokat
- Käyttöohje: järjestelmän asennus, käyttö ja ylläpito
- API-dokumentaatio: kaikki rajapinnat

## 8. Ylläpidettävyys ja päivitettävyys
- Mallin päivitysmahdollisuus ilman järjestelmän uudelleenasennusta
- Lokitiedostot diagnostiikkaa varten