# Visualization

Tämä hakemisto sisältää kaikki projektin visualisoinnit ja raportit.

## Visualisointien tyypit

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

### 5. Mallien analyysi
- `decisionBoundaries.png`: Mallien päätösrajapinnat
  - SVM, Random Forest ja XGBoost -mallien päätösrajapinnat
  - Luokkarajat visualisoituna feature-avaruudessa
- `confusionMatrices.png`: Mallien sekaannusmatriisit
  - Normalisoidut sekaannusmatriisit kaikille malleille
- `featureImportance.png`: Piirteiden tärkeys
  - Random Forest ja XGBoost -mallien piirteiden tärkeydet
- `rocCurves.png`: ROC-käyrät
  - ROC-käyrät kaikille malleille ja luokille
  - AUC-arvot
- `precisionRecallCurves.png`: Precision-Recall -käyrät
  - Precision-Recall -käyrät kaikille malleille ja luokille
  - Average Precision -arvot

### 6. Hydrauliikkadatan tarkkuustestaus
- `hydraulic_accuracy_*`: Aikaleimalla varustetut kansiot, jotka sisältävät:
  - `confusion_matrix.png`: Sekaannusmatriisi hydrauliikkadatalla
  - `class_distribution.png`: Luokkien jakauma hydrauliikkadatassa
  - `feature_scatterplot.png`: Ominaisuuksien scatter plot
  - `accuracy_report.txt`: Yksityiskohtainen tekstiraportti mallin tarkkuudesta

## Visualisointien luonti

Visualisoinnit luodaan automaattisesti seuraavien skriptien avulla:

1. Datan generointi ja analysointi: `generateData/`-kansion skriptit
2. Datan esikäsittely: `dataPreprocessing/`-kansion skriptit
3. Piirteiden analysointi: `featureEngineering/`-kansion skriptit
4. Mallien koulutus ja arviointi: `modelTraining/`-kansion skriptit
5. Mallien analyysi: `analyseModels/`-kansion skriptit
6. Hydrauliikkadatan tarkkuustestaus: `modelTraining/testHydraulicDataAccuracy.py`

## Visualisointien tarkastelu
- Kaikki visualisoinnit ovat PNG-muodossa (paitsi animaatiot, jotka ovat GIF-muodossa)
- Tekstiraportit ovat TXT-muodossa
- Suositeltu katseluohjelma: mikä tahansa kuvankatselin tai tekstieditori
