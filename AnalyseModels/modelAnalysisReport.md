# Mallien analyysi

## Yhteenveto

Tässä raportissa analysoidaan kolmea eri koneoppimismallia, jotka on koulutettu hydrauliikkajärjestelmän tilan luokitteluun:
- Support Vector Machine (SVM)
- Random Forest
- XGBoost

Analyysi keskittyy mallien suorituskykyyn, päätösrajapintoihin, sekaannusmatriiseihin, ROC-käyriin, Precision-Recall -käyriin sekä piirteiden tärkeyteen.

## Mallien suorituskyky

### Tarkkuus (Accuracy)

- **SVM**: 0.9906
- **Random Forest**: 0.9913
- **XGBoost**: 0.9906

### Makro-keskiarvot

| Malli | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| SVM | 0.9872 | 0.9896 | 0.9883 |
| Random Forest | 0.9876 | 0.9908 | 0.9890 |
| XGBoost | 0.9878 | 0.9889 | 0.9883 |

### Luokkakohtaiset metriikat


#### Makro-keskiarvo

| Malli | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| SVM | 0.9872 | 0.9896 | 0.9883 |
| Random Forest | 0.9876 | 0.9908 | 0.9890 |
| XGBoost | 0.9878 | 0.9889 | 0.9883 |

#### hose_break

| Malli | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| SVM | 1.0000 | 0.9799 | 0.9898 |
| Random Forest | 1.0000 | 0.9799 | 0.9898 |
| XGBoost | 1.0000 | 0.9799 | 0.9898 |

#### normal_digging

| Malli | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| SVM | 0.9945 | 0.9872 | 0.9909 |
| Random Forest | 0.9963 | 0.9872 | 0.9918 |
| XGBoost | 0.9927 | 0.9891 | 0.9909 |

#### normal_empty

| Malli | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| SVM | 1.0000 | 1.0000 | 1.0000 |
| Random Forest | 1.0000 | 1.0000 | 1.0000 |
| XGBoost | 1.0000 | 1.0000 | 1.0000 |

#### normal_full

| Malli | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| SVM | 0.9415 | 0.9833 | 0.9620 |
| Random Forest | 0.9418 | 0.9889 | 0.9648 |
| XGBoost | 0.9462 | 0.9778 | 0.9617 |

#### overload

| Malli | Precision | Recall | F1-score |
|-------|-----------|--------|----------|
| SVM | 1.0000 | 0.9978 | 0.9989 |
| Random Forest | 1.0000 | 0.9978 | 0.9989 |
| XGBoost | 1.0000 | 0.9978 | 0.9989 |

## Päätösrajapinnat

Päätösrajapintakuvaajat näyttävät, miten kukin malli jakaa syöteavaruuden eri luokkien alueisiin. Nämä kuvaajat auttavat visualisoimaan, miten mallit tekevät luokittelupäätöksiä pumpControl- ja pressure-muuttujien perusteella.

![Päätösrajapinnat](decisionBoundaries.png)

## Sekaannusmatriisit

Sekaannusmatriisit näyttävät, kuinka hyvin mallit luokittelevat eri tilat. Jokaisessa solussa oleva arvo kertoo, kuinka suuri osuus todellisen luokan näytteistä on luokiteltu ennustettuun luokkaan.

![Sekaannusmatriisit](confusionMatrices.png)

## ROC-käyrät

ROC-käyrät (Receiver Operating Characteristic) kuvaavat mallien kykyä erottaa eri luokat toisistaan. Käyrän alla oleva pinta-ala (AUC) kertoo mallin erottelukyvystä - mitä lähempänä arvoa 1, sitä parempi malli on.

![ROC-käyrät](rocCurves.png)

## Precision-Recall -käyrät

Precision-Recall -käyrät kuvaavat mallien tarkkuuden (precision) ja saannin (recall) välistä suhdetta eri kynnysarvoilla. Nämä käyrät ovat erityisen hyödyllisiä, kun luokkien jakaumat ovat epätasapainossa.

![Precision-Recall -käyrät](precisionRecallCurves.png)

## Piirteiden tärkeys

Piirteiden tärkeysvertailu näyttää, kuinka paljon eri syötemuuttujat vaikuttavat Random Forest ja XGBoost -mallien päätöksentekoon. SVM-mallille piirteiden tärkeyttä ei voida suoraan laskea samalla tavalla.

![Piirteiden tärkeys](featureImportance.png)

## Johtopäätökset

Analyysin perusteella voidaan tehdä seuraavat johtopäätökset:

1. Kaikki kolme mallia suoriutuvat erinomaisesti hydrauliikkajärjestelmän tilan luokittelussa, saavuttaen yli 99% tarkkuuden.
2. SVM-malli osoittautui hieman paremmaksi tarkkuuden osalta, mikä vahvistaa aiemman vertailun tulokset.
3. Random Forest ja XGBoost -mallien piirteiden tärkeysanalyysi osoittaa, että pressure-muuttuja on hieman tärkeämpi kuin pumpControl-muuttuja.
4. Mallien päätösrajapinnat ovat selkeitä, mikä viittaa siihen, että luokat ovat hyvin eroteltavissa toisistaan.
5. Sekaannusmatriisit osoittavat, että mallit tunnistavat erityisen hyvin normal_digging-, overload- ja hose_break-tilat.

Yhteenvetona voidaan todeta, että SVM-malli on paras valinta hydrauliikkajärjestelmän tilan luokitteluun, mutta myös Random Forest ja XGBoost -mallit tarjoavat erinomaisen suorituskyvyn.
