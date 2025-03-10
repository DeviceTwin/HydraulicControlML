# Hydrauliikkajärjestelmän tilan tunnistusmallin käyttöohje

Tämä dokumentti sisältää ohjeet hydrauliikkajärjestelmän tilan tunnistusmallin käyttöön. Malli tunnistaa viisi eri tilaa: normal_digging, normal_full, normal_empty, overload ja hose_break.

## Mallin käyttö Python-koodissa

Mallia voidaan käyttää Python-koodissa seuraavasti:

```python
import pickle
import numpy as np

# Lataa malli
def loadModel(modelPath):
    with open(modelPath, 'rb') as f:
        model = pickle.load(f)
    return model

# Ennusta tila
def predictState(model, pumpControl, pressure):
    # Varmista että arvot ovat välillä [0,1]
    pumpControl = max(0, min(1, pumpControl))
    pressure = max(0, min(1, pressure))
    
    # Tee ennuste
    X = np.array([[pumpControl, pressure]])
    state = model.predict(X)[0]
    
    # Hae todennäköisyydet jos malli tukee niitä
    probabilities = None
    if hasattr(model, 'predict_proba'):
        probabilities = model.predict_proba(X)[0]
    
    return state, probabilities

# Esimerkki käytöstä
modelPath = "path/to/best_SVM_model.pkl"
model = loadModel(modelPath)

# Esimerkkiarvot
pumpControl = 0.92  # Pumpun ohjausarvo (skaalattu välille 0-1)
pressure = 0.80     # Paine (skaalattu välille 0-1)

# Ennusta tila
state, probabilities = predictState(model, pumpControl, pressure)
print(f"Ennustettu tila: {state}")

# Jos todennäköisyydet ovat saatavilla, tulosta ne
if probabilities is not None:
    classNames = model.classes_
    for i, className in enumerate(classNames):
        print(f"{className}: {probabilities[i]:.4f}")
```

## Mallin käyttö komentorivillä

Voit käyttää mallia myös suoraan komentorivillä ajamalla modelPredict.py-tiedoston:

```
python modelPredict.py
```

Tämä skripti:
1. Lataa parhaan mallin Models-kansiosta
2. Visualisoi mallin päätösrajat ja tallentaa kuvan Visualization-kansioon
3. Näyttää esimerkkiennusteita eri syötearvoilla

## Syötemuuttujat

Malli käyttää kahta syötemuuttujaa:

1. **pumpControl** - Pumpun ohjausarvo (skaalattu välille 0-1)
2. **pressure** - Paine (skaalattu välille 0-1)

## Mallin tuloste

Malli palauttaa hydrauliikkajärjestelmän tilan, joka on yksi seuraavista:

- **normal_digging** - Normaali kaivuutila
- **normal_full** - Normaali täysi tila
- **normal_empty** - Normaali tyhjä tila
- **overload** - Ylikuormitustila
- **hose_break** - Letkurikkotila

## Vinkkejä mallin käyttöön

1. **Syötearvot**: Varmista, että syötearvot ovat skaalattu välille 0-1. Malli on koulutettu tällä skaalalla.
2. **Todennäköisyydet**: SVM-malli palauttaa myös luokkatodennäköisyydet, jotka voivat olla hyödyllisiä epävarmoissa tapauksissa.
3. **Visualisointi**: Voit visualisoida mallin päätösrajat käyttämällä modelPredict.py-tiedoston visualizePrediction-funktiota.
4. **Mallin päivitys**: Jos haluat päivittää mallia, aja ensin modelComparison.py luodaksesi uuden mallin ja sitten modelPredict.py testataksesi sitä.

## Mallin suorituskyky

SVM-malli valittiin parhaaksi malliksi, koska se saavutti korkeimman tarkkuuden (99.33%) testidatalla. Mallin optimaaliset hyperparametrit ovat:

- C = 100
- gamma = 'scale'
- kernel = 'rbf'

Ominaisuuksien tärkeysjärjestys:
- pressure: 0.56
- pumpControl: 0.44
