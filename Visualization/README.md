# Visualization

Tämä hakemisto sisältää datan analysoinnin ja prosessoinnin visualisointeja.

## Visualisoinnit

### Datan puhdistus
- `dataCleaningAnalysis.png`: Korruptoidun datan analyysi
  - Puuttuvien arvojen visualisointi
  - PumpControl outlierien visualisointi (<0 tai >100)
  - Pressure outlierien visualisointi (<0)
  - Luokkajakauman visualisointi

### Datan skaalaus
- `featureDistributions.png`: Feature-jakaumien visualisointi ennen skaalausta
  - PumpControl-muuttujan jakauma histogrammina
  - Pressure-muuttujan jakauma histogrammina
  - Auttaa ymmärtämään skaalauksen tarvetta

### Datan jako
- `dataSplitAnalysis.png`: Training/validation/test jaon visualisointi
  - A) Pie chart: Datan jako (70/15/15)
  - B) Feature-jakaumat skaalattuna välille [0,1]
  - C) Luokkajakaumat eri dataseteissä

### Hydraulic Analysis
- `hydraulicAnalysis.png` - Generoidun datan visualisointi.
