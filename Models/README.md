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

### Tulossa
- Luokittelumalli hydraulisen järjestelmän tilan tunnistamiseen
  * Input: pumpControl, pressure
  * Output: state (5 luokkaa)
  * Metriikka: accuracy, precision, recall, F1-score
  * Validointi: validation data (15%)
  * Testaus: test data (15%)
