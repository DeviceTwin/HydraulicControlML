# Feature Engineering

Tämä hakemisto sisältää työkaluja ja skriptejä hydraulisen järjestelmän datan piirteiden analysointiin ja muokkaamiseen.

## Tiedostot

### Korrelaatioanalyysi
- `correlationAnalysis.py`: Analysoi piirteiden välisiä korrelaatioita ja visualisoi tulokset
  - Luo korrelaatiomatriisin numeerisille muuttujille
  - Analysoi piirteiden korrelaatioita eri tilojen kanssa
  - Luo scatter plot -visualisaation pumpun ohjausarvon ja paineen suhteesta eri tiloissa
  - Tallentaa kaikki visualisaatiot Visualization-kansioon

## Käyttö

Suorita korrelaatioanalyysi komennolla:

```bash
python FeatureEngineering/correlationAnalysis.py
```

Analyysin tulokset tallennetaan seuraaviin tiedostoihin:
- `Visualization/correlationMatrix.png`: Numeeristen muuttujien korrelaatiomatriisi
- `Visualization/stateCorrelations.png`: Muuttujien korrelaatiot eri tilojen kanssa
- `Visualization/featureScatter.png`: Pumpun ohjausarvon ja paineen suhde eri tiloissa
