# FeatureEngineering

Tämä hakemisto sisältää työkaluja ja skriptejä hydraulisen järjestelmän datan piirteiden analysointiin ja muokkaamiseen.

## Jupyter Notebookit

### 1. correlationAnalysis.ipynb
- Piirteiden välisten korrelaatioiden analyysi
  * Numeeristen muuttujien välisten korrelaatioiden laskeminen
  * Numeeristen muuttujien ja luokkamuuttujien välisten korrelaatioiden analysointi
  * Pumpun ohjausarvon ja paineen suhteen visualisointi eri tiloissa
- Visualisoinnit:
  * Korrelaatiomatriisi numeerisille muuttujille
  * Heatmap numeeristen muuttujien ja tilamuuttujien välisistä korrelaatioista
  * Scatter plot pumpun ohjausarvon ja paineen suhteesta eri tiloissa
- Tallentaa:
  * `../Visualization/correlationMatrix.png`
  * `../Visualization/stateCorrelations.png`
  * `../Visualization/featureScatter.png`

## Käyttö

### Jupyter Notebook
1. Avaa Jupyter Notebook -ympäristö
2. Avaa `correlationAnalysis.ipynb`
3. Suorita solut järjestyksessä

## Tulokset ja johtopäätökset

Korrelaatioanalyysi paljastaa tärkeitä yhteyksiä hydraulisen järjestelmän muuttujien välillä:

1. **Numeeristen muuttujien väliset korrelaatiot:**
   - pumpControl ja pressure: vahva positiivinen korrelaatio (0.75)
   - pumpControl ja state_numeric: kohtalainen positiivinen korrelaatio (0.42)
   - pressure ja state_numeric: heikko positiivinen korrelaatio (0.16)

2. **Numeeristen muuttujien korrelaatiot eri tilojen kanssa:**
   - pressure ja state_overload: erittäin vahva positiivinen korrelaatio (0.83)
   - pumpControl ja state_overload: vahva positiivinen korrelaatio (0.67)
   - pressure ja state_hose_break: vahva negatiivinen korrelaatio (-0.52)

3. **Johtopäätökset:**
   - Ylikuormitustilanne (overload) on selkeimmin tunnistettavissa korkean paineen ja pumpun ohjausarvon avulla
   - Letkurikko (hose_break) tunnistettavissa alhaisen paineen avulla
   - Pumpun ohjausarvo ja paine ovat tärkeimmät piirteet järjestelmän tilan tunnistamisessa
