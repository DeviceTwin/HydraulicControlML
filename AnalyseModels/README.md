# Mallien analyysi

Tämä hakemisto sisältää työkalut ja tulokset hydrauliikkajärjestelmän koneoppimismallien kattavaan analyysiin.

## Sisältö

- `modelAnalysis.py` - Pääskripti mallien analysointiin
- `modelAnalysisReport.md` - Kattava raportti analyysin tuloksista
- `modelComparisonResults.csv` - Vertailutaulukko mallien suorituskyvystä
- Visualisointikuvat:
  - `decisionBoundaries.png` - Mallien päätösrajapinnat
  - `confusionMatrices.png` - Mallien sekaannusmatriisit
  - `featureImportance.png` - Piirteiden tärkeysvertailu
  - `rocCurves.png` - ROC-käyrät jokaiselle mallille ja luokalle
  - `precisionRecallCurves.png` - Precision-Recall -käyrät

## Käyttö

Suorita analyysi ajamalla:

```
python modelAnalysis.py
```

Skripti lataa tallennetut mallit (SVM, Random Forest, XGBoost) ja testidatan, suorittaa kattavan analyysin ja tallentaa tulokset tähän hakemistoon.

## Analyysin sisältö

Analyysi sisältää seuraavat osa-alueet:

1. **Mallien suorituskyky** - Tarkkuus, precision, recall ja F1-score jokaiselle mallille ja luokalle
2. **Päätösrajapinnat** - Visualisointi siitä, miten mallit jakavat syöteavaruuden eri luokkien alueisiin
3. **Sekaannusmatriisit** - Näyttävät, kuinka hyvin mallit luokittelevat eri tilat
4. **ROC-käyrät** - Kuvaavat mallien kykyä erottaa eri luokat toisistaan
5. **Precision-Recall -käyrät** - Kuvaavat mallien tarkkuuden ja saannin välistä suhdetta
6. **Piirteiden tärkeys** - Vertailu siitä, kuinka paljon eri syötemuuttujat vaikuttavat mallien päätöksentekoon

## Johtopäätökset

Katso kattavat johtopäätökset ja suositukset tiedostosta `modelAnalysisReport.md`.
