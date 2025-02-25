# Hydraulic Control Data

Tämä hakemisto sisältää hydraulisen järjestelmän dataa eri prosessointivaiheissa.

## Tiedostot

### Alkuperäinen data
- `hydraulicData.csv`: Alkuperäinen simuloitu hydraulidata
  - Sarakkeet: pumpControl, pressure, state
  - Rivejä: 10000
  - Tilajakauma:
    * normal_digging: ~37%
    * overload: ~30%
    * normal_full: ~12%
    * normal_empty: ~11%
    * hose_break: ~10%

### Prosessoidut datat
1. `corruptedHydraulicData.csv`: Korruptoitu data testaamista varten
   - Lisätty puuttuvia arvoja: 40 kpl
   - Lisätty outlier-arvoja:
     * pumpControl: 28 kpl (<0 tai >100)
     * pressure: 8 kpl (<0)
   - Rivejä: 10000

2. `cleanHydraulicData.csv`: Puhdistettu data
   - Poistettu puuttuvat arvot ja outlierit
   - Rivejä: 9924
   - Ei puuttuvia arvoja
   - Kaikki arvot validilla alueella
   - Tilajakauma säilytetty

3. `scaledHydraulicData.csv`: Skaalattu data
   - MinMaxScaler käytetty
   - Kaikki numeeriset arvot skaalattu välille [0,1]
   - Rivejä: 9924

### Jaetut datasetit koneoppimista varten
1. `trainingData.csv`: Training data (70%)
   - Rivejä: 6946
   - Luokkajakauma:
     * normal_digging: 2563 kpl
     * overload: 2087 kpl
     * normal_full: 835 kpl
     * normal_empty: 769 kpl
     * hose_break: 692 kpl

2. `validationData.csv`: Validation data (15%)
   - Rivejä: 1489
   - Luokkajakauma säilytetty samana kuin training datassa

3. `testData.csv`: Test data (15%)
   - Rivejä: 1489
   - Luokkajakauma säilytetty samana kuin training datassa

## Datan rakenne

### Sarakkeet
- `pumpControl`: Pumpun ohjausarvo
  * Raakadata: [0,100]
  * Skaalattu: [0,1]
- `pressure`: Järjestelmän paine
  * Raakadata: [0,450]
  * Skaalattu: [0,1]
- `state`: Järjestelmän tila (luokka)
  * normal_digging: Normaali kaivuutoiminta
  * overload: Ylikuormitustilanne
  * normal_full: Täyden kauhan liikkeet
  * normal_empty: Tyhjän kauhan liikkeet
  * hose_break: Letkurikko
