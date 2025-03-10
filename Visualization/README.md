# Visualization

Tämä hakemisto sisältää datan analysoinnin ja prosessoinnin visualisointeja.

## Visualisoinnit

### 1. Datan generointi
- `hydraulicAnalysis.png`: Generoidun datan visualisointi
  - A) Scatter plot: pumpControl vs. pressure eri tiloissa
  - B) Pie chart: Tilojen jakauma datassa
  - C) Density plot: pumpControl-jakauma tiloittain
  - D) Density plot: pressure-jakauma tiloittain

### 2. Datan puhdistus
- `corruptedMissingValues.png`: Puuttuvien arvojen visualisointi
  - Heatmap: Puuttuvien arvojen sijainnit
  - Bar plot: Puuttuvien arvojen määrä sarakkeittain
- `corruptedOutliersValues.png`: Poikkeavien havaintojen visualisointi
  - Box plot: pumpControl ja pressure -muuttujien jakaumat
  - Scatter plot: Outlier-havainnot korostettuna
- `dataCleaningAnalysis.png`: Puhdistuksen vaikutukset
  - Feature-jakaumien muutokset
  - Luokkajakauman säilyminen
  - Poistettujen rivien analyysi

### 3. Datan skaalaus ja jako
- `featureDistributions.png`: Feature-jakaumien visualisointi
  - Histogrammit ennen skaalausta
  - Histogrammit skaalauksen jälkeen
  - Q-Q plotit normaalisuuden tarkistamiseen
- `dataSplitAnalysis.png`: Training/validation/test jaon visualisointi
  - A) Pie chart: Datan jako (70/15/15)
  - B) Bar plot: Luokkajakaumat eri seteissä
  - C) Box plot: Feature-jakaumat eri seteissä

### 4. Mallien suorituskyky
- `learningCurves.png`: Mallien oppimiskäyrät
  - SVM, Random Forest ja XGBoost -mallien oppimiskäyrät
  - Koulutusdatan koon vaikutus mallien tarkkuuteen
  - Ylisovittamisen ja alisovittamisen tunnistaminen
- `hyperparameterEffects.png`: Hyperparametrien vaikutukset
  - SVM: C-parametrin vaikutus tarkkuuteen
  - Random Forest: n_estimators-parametrin vaikutus tarkkuuteen
  - XGBoost: max_depth-parametrin vaikutus tarkkuuteen
- `model_comparisons.png`: Mallien vertailu
  - Sekaannusmatriisit kaikille malleille
  - Mallien tarkkuuksien vertailu pylväsdiagrammina

## Käyttö

### Visualisointien luonti
- Generoidun datan visualisoinnit: `GenerateData.ipynb`
- Puhdistuksen visualisoinnit: `CorruptedVisualizeData.ipynb` ja `CheckCleanData.ipynb`
- Skaalauksen ja jaon visualisoinnit: `SplitVisualizeData.ipynb`
- Mallien suorituskyvyn visualisoinnit: `modelTraining.ipynb`

### Visualisointien tarkastelu
- Kaikki visualisoinnit ovat PNG-muodossa
- Suositeltu katseluohjelma: mikä tahansa kuvankatselin
- Visualisointien resoluutio: 1200x800 pikseliä
