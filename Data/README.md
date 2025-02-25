# Hydraulic Control Data

Tämä hakemisto sisältää hydraulisen järjestelmän dataa eri prosessointivaiheissa.

## Tiedostot

### Alkuperäinen data
- `hydraulicData.csv`: Alkuperäinen simuloitu hydraulidata
  - Sarakkeet: pumpControl, pressure, state
  - Rivejä: 10000

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

3. `scaledHydraulicData.csv`: Skaalattu data
   - MinMaxScaler käytetty
   - Kaikki numeeriset arvot skaalattu välille [0,1]
   - Rivejä: 9924

### Jaetut datasetit koneoppimista varten
1. `trainingData.csv`: Training data (70%)
   - Rivejä: 6946
   - Luokkajakauma:
     * normal_digging: 2564
     * overload: 2080
     * normal_full: 837
     * normal_empty: 772
     * hose_break: 693

2. `validationData.csv`: Validation data (15%)
   - Rivejä: 1489
   - Luokkajakauma säilytetty samana kuin training datassa

3. `testData.csv`: Test data (15%)
   - Rivejä: 1489
   - Luokkajakauma säilytetty samana kuin training datassa

## Datan rakenne

### Sarakkeet
- `pumpControl`: Pumpun ohjausarvo [0,1]
- `pressure`: Järjestelmän paine [0,1]
- `state`: Järjestelmän tila (luokka)
  * normal_digging
  * overload
  * normal_full
  * normal_empty
  * hose_break
