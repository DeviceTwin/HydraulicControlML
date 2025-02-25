# DataPreprocessing
Tässä hakemistossa suoritetaan datan esikäsittely ja visualisointi.

## Tiedostot
- `CorruptedVisualizeData.ipynb` - Jupyter notebook, jolla luodaan korruptoitua dataa ja visualisoidaan sitä
- `CheckCleanData.ipynb` - Jupyter notebook, joka tarkistaa ja puhdistaa datan puuttuvista arvoista ja poikkeavista havainnoista
- `../Data/corruptedHydraulicData.csv` - Korruptoitu data puuttuvilla arvoilla ja poikkeavilla havainnoilla
- `../Data/cleanHydraulicData.csv` - Puhdistettu data ilman puuttuvia arvoja ja poikkeavia havaintoja

## Datan korruptointi
- Dataan lisätään puuttuvia arvoja (NaN) ja poikkeavia havaintoja (outliers)
- Puuttuvien arvojen ja poikkeavien havaintojen visualisointi
- Tallentaa virheitä sisältyvän datan tiedostoon `../Data/corruptedHydraulicData.csv`
- Tallentaa puuttuvien arvojen visualisoinnin tiedostoon `../Visualization/corruptedMissingValues.png`
- Tallentaa poikkeavien havaintojen visualisoinnin tiedostoon `../Visualization/corruptedOutliersValues.png`

## Datan puhdistus
- Tarkistaa puuttuvat arvot ja poikkeavat havainnot ja visualisoi ne
- Tallentaa puuttuvien arvojen visualisoinnin tiedostoon `../Visualization/missingValuesAnalysis.png`
- Tallentaa poikkeavien havaintojen visualisoinnin tiedostoon `../Visualization/outliersValuesAnalysis.png`
- Poistaa rivit, joissa on puuttuvia arvoja
- Poistaa rivit, joissa on poikkeavia havainnoita (pumpControl < 0 tai > 100, pressure < 0)
- Tallentaa puhdistetun datan tiedostoon `../Data/cleanHydraulicData.csv`
- Tulostaa yhteenvedon datan tilasta ennen ja jälkeen puhdistuksen

## Käyttö
1. Valitse Kerneliksi **Python 3.x**
2. Aja `CorruptedVisualizeData.ipynb` notebook lisätäksesi dataan virheitä
3. Aja `CheckCleanData.ipynb` notebook datan puhdistamiseksi
   
   