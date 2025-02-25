# HydraulicControlML
Mallin avulla valvotaan ja estetään kuvitteellisen työkoneen hydraulijärjestelmän vikojen ja ongelmien aiheuttamat vahingot.
https://www.youtube.com/watch?v=eViLZylQ3qM&t=372s


## Hakemistot
Projektin rakenne ja sisältö:

- `GenerateData/` - Hydraulisen järjestelmän datan generointi ja analysointi. Sisältää toiminnallisuuden eri työtilojen (normaali kaivuu, ylikuormitus, letkurikko) datan luomiseen sekä monipuoliset visualisoinnit ja tilastolliset analyysit.
- `DataPreprocessing/` - Datan esikäsittely:
  - Datan korruptointi (puuttuvat arvot ja poikkeavat havainnot)
  - Datan puhdistus ja visualisointi
  - Datan skaalaus
  - Datan jako koneoppimista varten
- `Data/` - CSV tiedostot:
  - Generoitu raakadata
  - Korruptoitu data
  - Puhdistettu data
  - Skaalattu data
  - Training/validation/test datasetit
- `Models/` - Koneoppimismallit ja esikäsittelykomponentit:
  - MinMaxScaler-malli datan skaalaukseen
  - Koneoppimismallit (tulossa)
- `Visualization/` - Datan visualisoinnit:
  - Generoidun datan kuvaajat
  - Puuttuvien arvojen visualisoinnit
  - Poikkeavien havaintojen visualisoinnit
  - Feature-jakaumien visualisoinnit
  - Datan jako-analyysi

## Työnkulku
1. Datan generointi (`GenerateData/`)
   - Normaalit toimintatilat (tyhjä kauha, normaali kaivuu, täysi kauha)
   - Vikatilat (ylikuormitus, letkurikko)
2. Datan korruptointi ja visualisointi (`DataPreprocessing/`)
3. Datan tarkistus ja puhdistus (`DataPreprocessing/`)
4. Datan skaalaus ja jako (`DataPreprocessing/`)
5. Koneoppimismallien kehitys (tulossa)

## Lisenssi
Tämä projekti on lisensoitu avoimen lähdekoodin lisenssillä (MIT).
