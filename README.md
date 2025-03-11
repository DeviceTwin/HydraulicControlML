# HydraulicControlML
Mallin avulla valvotaan ja estetään kuvitteellisen työkoneen hydraulijärjestelmän vikojen ja ongelmien aiheuttamat vahingot.
https://www.youtube.com/watch?v=eViLZylQ3qM&t=372s


## Hakemistot
Projektin rakenne ja sisältö:

- `generateData/` - Hydraulisen järjestelmän datan generointi ja analysointi. Sisältää toiminnallisuuden eri työtilojen (normaali kaivuu, ylikuormitus, letkurikko) datan luomiseen sekä monipuoliset visualisoinnit ja tilastolliset analyysit.
- `dataPreprocessing/` - Datan esikäsittely:
  - Datan korruptointi (puuttuvat arvot ja poikkeavat havainnot)
  - Datan puhdistus ja visualisointi
  - Datan skaalaus
  - Datan jako koneoppimista varten
- `featureEngineering/` - Piirteiden analysointi ja muokkaus:
  - Piirteiden välisten korrelaatioiden analysointi
  - Numeeristen muuttujien ja luokkamuuttujien välisten suhteiden visualisointi
  - Piirteiden merkittävyyden arviointi koneoppimismalleja varten
- `modelTraining/` - Koneoppimismallien koulutus ja arviointi:
  - SVM, Random Forest ja XGBoost -mallien koulutus
  - Mallien suorituskyvyn arviointi (tarkkuus, sekaannusmatriisit)
  - Oppimiskäyrien visualisointi
  - Hyperparametrien vaikutusten analysointi
  - Mallin tarkkuuden testaus hydrauliikkadatalla
- `analyseModels/` - Mallien kattava analyysi:
  - Päätösrajapintojen visualisointi
  - Sekaannusmatriisien tarkempi analyysi
  - ROC- ja Precision-Recall -käyrien analysointi
  - Piirteiden tärkeyden vertailu
- `data/` - CSV tiedostot:
  - Generoitu raakadata
  - Korruptoitu data
  - Puhdistettu data
  - Skaalattu data
  - Training/validation/test datasetit
- `models/` - Koneoppimismallit ja esikäsittelykomponentit:
  - MinMaxScaler-malli datan skaalaukseen
  - Koulutetut mallit (SVM, Random Forest, XGBoost)
- `visualization/` - Kaikki projektin visualisoinnit ja raportit:
  - Generoidun datan kuvaajat
  - Puuttuvien arvojen visualisoinnit
  - Poikkeavien havaintojen visualisoinnit
  - Feature-jakaumien visualisoinnit
  - Datan jako-analyysi
  - Korrelaatiomatriisit ja scatter plot -visualisoinnit
  - Mallien oppimiskäyrät ja suorituskykyvertailut
  - Mallien tarkkuusraportit ja sekaannusmatriisit
  - Päätösrajapintojen visualisoinnit
  - ROC- ja Precision-Recall -käyrät

## Työnkulku
1. Datan generointi (`generateData/`)
   - Normaalit toimintatilat (tyhjä kauha, normaali kaivuu, täysi kauha)
   - Vikatilat (ylikuormitus, letkurikko)
2. Datan korruptointi ja visualisointi (`dataPreprocessing/`)
3. Datan tarkistus ja puhdistus (`dataPreprocessing/`)
4. Datan skaalaus ja jako (`dataPreprocessing/`)
5. Piirteiden analysointi ja korrelaatiot (`featureEngineering/`)
6. Koneoppimismallien koulutus ja arviointi (`modelTraining/`)
   - Mallien koulutus (SVM, Random Forest, XGBoost)
   - Mallien suorituskyvyn arviointi ja vertailu
   - Parhaan mallin valinta (SVM)
   - Mallin tarkkuuden testaus hydrauliikkadatalla
7. Mallien kattava analyysi (`analyseModels/`)
   - Päätösrajapintojen visualisointi
   - Sekaannusmatriisien tarkempi analyysi
   - ROC- ja Precision-Recall -käyrien analysointi

## Lisenssi
Tämä projekti on lisensoitu avoimen lähdekoodin lisenssillä (MIT).
