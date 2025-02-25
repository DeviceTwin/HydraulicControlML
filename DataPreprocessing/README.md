# DataPreprocessing

Tämä hakemisto sisältää datan esikäsittelyyn liittyvät Jupyter Notebookit ja dokumentaation.

## Jupyter Notebookit

### 1. CorruptedVisualizeData.ipynb
- Datan korruptointi testaamista varten
  * Lisää puuttuvia arvoja (NaN) satunnaisiin kohtiin
  * Lisää poikkeavia havaintoja (outliers) pumpControl ja pressure -muuttujiin
- Korruptoidun datan visualisointi
  * Puuttuvien arvojen sijainnit
  * Poikkeavien havaintojen jakaumat
  * Luokkajakauman säilyminen
- Tallentaa:
  * `../Data/corruptedHydraulicData.csv`
  * `../Visualization/corruptedMissingValues.png`
  * `../Visualization/corruptedOutliersValues.png`

### 2. CheckCleanData.ipynb
- Datan puhdistus ja tarkistus
  * Puuttuvien arvojen poisto
  * Poikkeavien havaintojen suodatus
  * Luokkajakauman validointi
- Puhdistetun datan visualisointi
  * Feature-jakaumien vertailu
  * Luokkajakauman muutokset
- Tallentaa:
  * `../Data/cleanHydraulicData.csv`
  * `../Visualization/dataCleaningAnalysis.png`

### 3. SplitVisualizeData.ipynb
- Datan skaalaus ja jako
  * MinMaxScaler-mallin luonti ja sovitus
  * Datan jako training/validation/test setteihin (70/15/15)
  * Luokkajakauman säilyttäminen kaikissa seteissä
- Skaalatun datan visualisointi
  * Feature-jakaumien vertailu ennen ja jälkeen skaalauksen
  * Luokkajakauman validointi eri seteissä
- Tallentaa:
  * `../Data/scaledHydraulicData.csv`
  * `../Data/trainingData.csv`
  * `../Data/validationData.csv`
  * `../Data/testData.csv`
  * `../Models/hydraulicScaler.joblib`
  * `../Visualization/featureDistributions.png`
  * `../Visualization/dataSplitAnalysis.png`

## Käyttö

1. Asenna tarvittavat kirjastot:
   ```bash
   pip install pandas numpy matplotlib seaborn scikit-learn
   ```

2. Suorita notebookit järjestyksessä:
   ```bash
   jupyter notebook CorruptedVisualizeData.ipynb
   jupyter notebook CheckCleanData.ipynb
   jupyter notebook SplitVisualizeData.ipynb
   ```

3. Tarkista tulokset:
   - Visualisoinnit: `../Visualization/`
   - Prosessoidut datat: `../Data/`
   - Mallit: `../Models/`