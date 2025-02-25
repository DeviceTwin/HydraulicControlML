# HydraulicControlML
Valvotaan kuvitteellisen työkoneen hydrauliikkajärjestelmää.

## Hakemistot
Projektin rakenne ja sisältö:

- `GenerateData/` - Jupyter Notebook hydraulisen järjestelmän datan generointiin ja analysointiin. Sisältää toiminnallisuuden eri työtilojen (normaali kaivuu, ylikuormitus, letkurikko) datan luomiseen sekä monipuoliset visualisoinnit ja tilastolliset analyysit.
- `DataPreprocessing/` - Jupyter Notebookit datan esikäsittelyyn:
  - Datan korruptointi (puuttuvat arvot ja poikkeavat havainnot)
  - Datan puhdistus ja visualisointi
  - Puhdistetun datan tallennus jatkokäsittelyä varten
- `Data/` - Sisältää kaikki csv tiedostot:
  - Generoitu raakadata
  - Korruptoitu data
  - Puhdistettu data
- `Visualization/` - Sisältää kaikki datan visualisoinnit:
  - Generoidun datan kuvaajat
  - Puuttuvien arvojen visualisoinnit
  - Poikkeavien havaintojen visualisoinnit

## Työnkulku
1. Datan generointi (`GenerateData/`)
2. Datan korruptointi ja visualisointi (`DataPreprocessing/CorruptedVisualizeData.ipynb`)
3. Datan tarkistus ja puhdistus (`DataPreprocessing/CheckCleanData.ipynb`)
4. Puhdistetun datan käyttö jatkoanalyyseihin

## Lisenssi
Tämä projekti on lisensoitu avoimen lähdekoodin lisenssillä (MIT).
