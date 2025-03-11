# ModelPredict.py - Käyttöohje

Tämä dokumentti sisältää ohjeet `modelPredict.py`-skriptin käyttöön hydrauliikkajärjestelmän tilan ennustamisessa. Skripti käyttää koulutettua SVM-mallia tunnistamaan järjestelmän tilan annettujen syötteiden perusteella.

## Yleiskatsaus

`modelPredict.py` on Python-skripti, joka:
1. Lataa koulutetun SVM-mallin ja skaalauskomponentin
2. Ottaa vastaan käyttäjän syöttämät pumpControl- ja pressure-arvot
3. Skaalaa arvot välille [0, 1]
4. Ennustaa hydrauliikkajärjestelmän tilan
5. Näyttää tulokset käyttäjälle

## Vaatimukset

Skriptin käyttämiseen tarvitaan:
- Python 3.6 tai uudempi
- Seuraavat Python-kirjastot:
  - pandas
  - numpy
  - scikit-learn
  - joblib
- Koulutettu SVM-malli (`SVM.pkl`) Models-kansiossa
- Skaalauskomponentti (`hydraulicScaler.joblib`) Models-kansiossa

## Skriptin käyttö

### Suorittaminen komentorivillä

Skriptin voi suorittaa komentorivillä seuraavasti:

```
python modelPredict.py
```

Skripti kysyy käyttäjältä kaksi syötearvoa:
1. **pumpControl** - Pumpun ohjausarvo (sallittu alue: 18-101)
2. **pressure** - Painearvo (sallittu alue: 1-432)

Esimerkki käytöstä:
```
Hydrauliikkajärjestelmän tilan ennustus
========================================
Syötä pumpControl-arvo (18-101): 75
Syötä pressure-arvo (1-432): 250

Syötetyt arvot: pumpControl=75, pressure=250
Skaalatut arvot: pumpControl=0.686747, pressure=0.577982
Numeerinen ennuste: 1
Tekstimuotoinen ennuste: normal_digging

Ennustettu tila: normal_digging
```

### Käyttö Python-koodissa

Skriptiä voi käyttää myös osana muuta Python-koodia importoimalla sen funktiot:

```python
from modelPredict import predictState

# Esimerkkiarvot
pumpControl = 75
pressure = 250

# Ennusta tila
state = predictState(pumpControl, pressure)
print(f"Ennustettu tila: {state}")
```

## Funktiot

### loadModelAndScaler()

Lataa SVM-mallin, skaalauskomponentin ja luokkien koodaajan.

**Palautusarvot:**
- `model`: Ladattu SVM-malli
- `scaler`: Ladattu skaalauskomponentti
- `labelEncoder`: Ladattu luokkien koodaaja

### predictState(pumpControl, pressure)

Ennustaa hydrauliikkajärjestelmän tilan annettujen arvojen perusteella.

**Parametrit:**
- `pumpControl`: Pumpun ohjausarvo (18-101)
- `pressure`: Painearvo (1-432)

**Palautusarvo:**
- `state`: Ennustettu tila (normal_digging, normal_full, normal_empty, overload, hose_break)

## Syötemuuttujat

Skripti käyttää kahta syötemuuttujaa:

1. **pumpControl** - Pumpun ohjausarvo
   - Sallittu alue: 18-101
   - Skaalataan automaattisesti välille [0, 1]

2. **pressure** - Painearvo
   - Sallittu alue: 1-432
   - Skaalataan automaattisesti välille [0, 1]

## Mallin tuloste

Malli palauttaa hydrauliikkajärjestelmän tilan, joka on yksi seuraavista:

- **normal_digging** - Normaali kaivuutila
- **normal_full** - Normaali täysi tila
- **normal_empty** - Normaali tyhjä tila
- **overload** - Ylikuormitustila
- **hose_break** - Letkurikkotila

## Virheenkäsittely

Skripti sisältää seuraavat virheenkäsittelyt:

1. **Syötteiden tarkistus**: Varoittaa, jos syötetyt arvot ovat sallitun alueen ulkopuolella, mutta jatkaa silti ennustusta skaalaamalla arvot välille [0, 1].

2. **Mallin latausvirheet**: Näyttää virheilmoituksen, jos mallia tai skaalauskomponenttia ei voida ladata.

3. **Syöttövirheet**: Käsittelee virheet, jos käyttäjä syöttää epäkelvon arvon (esim. kirjaimia numeroiden sijaan).

## Vinkkejä

1. **Syötearvot**: Varmista, että syötearvot ovat sallitulla alueella (pumpControl: 18-101, pressure: 1-432).

2. **Debug-tiedot**: Skripti näyttää debug-tietoja, kuten skaalatut arvot ja numeerisen ennusteen, mikä auttaa ymmärtämään mallin toimintaa.

3. **Integrointi**: Jos haluat integroida mallin muuhun järjestelmään, voit käyttää `predictState`-funktiota suoraan Python-koodissasi.

4. **Mallin päivitys**: Jos malli päivitetään, varmista että uusi malli tallennetaan samalla nimellä (`SVM.pkl`) Models-kansioon.

## Esimerkki tulosteesta

```
Hydrauliikkajärjestelmän tilan ennustus
========================================
Syötä pumpControl-arvo (18-101): 90
Syötä pressure-arvo (1-432): 400

Syötetyt arvot: pumpControl=90, pressure=400
Skaalatut arvot: pumpControl=0.867470, pressure=0.925810
Numeerinen ennuste: 3
Tekstimuotoinen ennuste: normal_full

Ennustettu tila: normal_full
```
