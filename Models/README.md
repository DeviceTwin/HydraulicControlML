# Models

Tämä hakemisto sisältää koneoppimismalleja ja niihin liittyviä komponentteja.

## Esikäsittelymallit

### MinMaxScaler
- `hydraulicScaler.joblib`: Datan skaalaukseen käytetty malli
  - Skaalaa numeeriset arvot välille [0,1]
  - Muunnoskaavat:
    * pumpControl: x_scaled = (x - min) / (max - min)
      - min = 0.0, max = 100.0
    * pressure: x_scaled = (x - min) / (max - min)
      - min = 0.0, max = 450.0
  - Käytetty `Data/cleanHydraulicData.csv` datan skaalaukseen
  - Tuottaa `Data/scaledHydraulicData.csv` tiedoston

## Koneoppimismallit

### Support Vector Machine (SVM)
- `svmModel.joblib`: Koulutettu SVM-malli hydraulisen järjestelmän tilan luokitteluun
  - Hyperparametrit: C=100, gamma='scale', kernel='rbf'
  - Tarkkuus: 99.33%
  - Input: pumpControl, pressure
  - Output: state (5 luokkaa)

### Random Forest
- `rfModel.joblib`: Koulutettu Random Forest -malli
  - Hyperparametrit: n_estimators=100, max_depth=None
  - Tarkkuus: 99.13%
  - Input: pumpControl, pressure
  - Output: state (5 luokkaa)

### XGBoost
- `xgbModel.joblib`: Koulutettu XGBoost-malli
  - Hyperparametrit: max_depth=5, learning_rate=0.1
  - Tarkkuus: 98.93%
  - Input: pumpControl, pressure
  - Output: state (5 luokkaa)

## Mallien vertailu

Mallien vertailu osoittaa, että SVM-malli suoriutuu parhaiten hydraulisen järjestelmän tilan luokittelussa. Ominaisuuksien tärkeydessä pressure (0.56) oli hieman tärkeämpi kuin pumpControl (0.44).

Visualisoinnit mallien suorituskyvystä löytyvät `Visualization`-hakemistosta:
- `learningCurves.png`: Mallien oppimiskäyrät
- `hyperparameterEffects.png`: Hyperparametrien vaikutukset mallien suorituskykyyn
- `model_comparisons.png`: Mallien sekaannusmatriisit ja tarkkuusvertailu
