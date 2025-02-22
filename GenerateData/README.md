# GenerateData
Generoidaan kuvitteellisen työkoneen testidataa.

## Tiedostot
- `GenerateData.ipynb` - Jupyter notebook, jolla voidaan generoida dataa ja visualisoida generoitu data.
- `../Visualization/hydraulic_analysis.png` - Generoidun datan visualisointigraafit.
- `../Data/hydraulic_data.csv` - Generoitu data csv tiedostona.

| pumpControl | pressure | state     |
|-------------|----------|-----------|
| 37          | 22       | normal    |
| 79         | 88       | overload  |
| 76         | 84       | overload  |
| 91         | 0        | hose_break|


## Käyttö
- Valitse Kerneliksi **Python 3.12.8** ja aja `GenerateData.ipynb`.
- Ajon tuloksena generoituu
- `../Data/hydraulic_data.csv`
- `../Visualization/hydraulic_analysis.png`
