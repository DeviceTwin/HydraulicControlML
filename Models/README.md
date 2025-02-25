# Models

Tämä hakemisto sisältää koneoppimismalleja ja niihin liittyviä komponentteja.

## Mallit

### Esikäsittelymallit
- `hydraulic_scaler.joblib`: MinMaxScaler-malli datan skaalaukseen
  - Skaalaa numeeriset arvot välille [0,1]
  - Muunnoskaavat:
    * pumpControl: x_scaled = (x - 0.220) * 0.012195
    * pressure: x_scaled = (x - 0.002) * 0.002320
  - Käytetty `Data/cleanHydraulicData.csv` datan skaalaukseen
  - Tuottaa `Data/scaledHydraulicData.csv` tiedoston

### Koneoppimismallit
- *Tulossa myöhemmin*
