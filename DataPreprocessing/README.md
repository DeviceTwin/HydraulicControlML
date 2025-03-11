# dataPreprocessing

Tämä hakemisto sisältää datan esikäsittelyyn liittyvät Jupyter Notebookit ja dokumentaation.

## Jupyter Notebookit

### 1. corruptedVisualizeData.ipynb
- Datan korruptointi testaamista varten
  * Lisää puuttuvia arvoja (NaN) satunnaisiin kohtiin
  * Lisää poikkeavia havaintoja (outliers) pumpControl ja pressure -muuttujiin
- Korruptoidun datan visualisointi
  * Puuttuvien arvojen sijainnit
  * Poikkeavien havaintojen jakaumat
  * Luokkajakauman säilyminen
- Tallentaa:
  * `../data/corruptedHydraulicData.csv`
  * `../visualization/corruptedMissingValues.png`
  * `../visualization/corruptedOutliersValues.png`

### 2. checkCleanData.ipynb
- Datan puhdistus ja tarkistus
  * Puuttuvien arvojen poisto
  * Poikkeavien havaintojen suodatus
  * Luokkajakauman validointi
- Puhdistetun datan visualisointi
  * Feature-jakaumien vertailu
  * Luokkajakauman muutokset
- Tallentaa:
  * `../data/cleanHydraulicData.csv`
  * `../visualization/dataCleaningAnalysis.png`

### 3. splitVisualizeData.ipynb
- Datan skaalaus ja jako
  * MinMaxScaler-mallin luonti ja sovitus
  * Datan jako training/validation/test setteihin (70/15/15)
  * Luokkajakauman säilyttäminen kaikissa seteissä
- Skaalatun datan visualisointi
  * Feature-jakaumien vertailu ennen ja jälkeen skaalauksen
  * Luokkajakauman validointi eri seteissä
- Tallentaa:
  * `../data/scaledHydraulicData.csv`
  * `../data/trainingData.csv`
  * `../data/validationData.csv`
  * `../data/testData.csv`
  * `../models/hydraulicScaler.joblib`
  * `../visualization/featureDistributions.png`
  * `../visualization/dataSplitAnalysis.png`

## Käyttö

1. Asenna tarvittavat kirjastot:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

2. Suorita notebookit järjestyksessä:
   ```bash
   jupyter notebook corruptedVisualizeData.ipynb
   jupyter notebook checkCleanData.ipynb
   jupyter notebook splitVisualizeData.ipynb
   ```

3. Tarkista tulokset:
   - Visualisoinnit: `../visualization/`
   - Prosessoidut datat: `../data/`
   - Mallit: `../models/`