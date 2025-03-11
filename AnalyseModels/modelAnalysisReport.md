# Mallien analyysi

## Yhteenveto

T�ss� raportissa analysoidaan kolmea eri koneoppimismallia, jotka on koulutettu hydrauliikkaj�rjestelm�n tilan luokitteluun:
- Support Vector Machine (SVM)
- Random Forest
- XGBoost

Analyysi keskittyy mallien suorituskykyyn, p��t�srajapintoihin, sekaannusmatriiseihin, ROC-k�yriin, Precision-Recall -k�yriin sek� piirteiden t�rkeyteen.

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

## P��t�srajapinnat

P��t�srajapintakuvaajat n�ytt�v�t, miten kukin malli jakaa sy�teavaruuden eri luokkien alueisiin. N�m� kuvaajat auttavat visualisoimaan, miten mallit tekev�t luokittelup��t�ksi� pumpControl- ja pressure-muuttujien perusteella.

![P��t�srajapinnat](decisionBoundaries.png)

## Sekaannusmatriisit

Sekaannusmatriisit n�ytt�v�t, kuinka hyvin mallit luokittelevat eri tilat. Jokaisessa solussa oleva arvo kertoo, kuinka suuri osuus todellisen luokan n�ytteist� on luokiteltu ennustettuun luokkaan.

![Sekaannusmatriisit](confusionMatrices.png)

## ROC-k�yr�t

ROC-k�yr�t (Receiver Operating Characteristic) kuvaavat mallien kyky� erottaa eri luokat toisistaan. K�yr�n alla oleva pinta-ala (AUC) kertoo mallin erottelukyvyst� - mit� l�hemp�n� arvoa 1, sit� parempi malli on.

![ROC-k�yr�t](rocCurves.png)

## Precision-Recall -k�yr�t

Precision-Recall -k�yr�t kuvaavat mallien tarkkuuden (precision) ja saannin (recall) v�list� suhdetta eri kynnysarvoilla. N�m� k�yr�t ovat erityisen hy�dyllisi�, kun luokkien jakaumat ovat ep�tasapainossa.

![Precision-Recall -k�yr�t](precisionRecallCurves.png)

## Piirteiden t�rkeys

Piirteiden t�rkeysvertailu n�ytt��, kuinka paljon eri sy�temuuttujat vaikuttavat Random Forest ja XGBoost -mallien p��t�ksentekoon. SVM-mallille piirteiden t�rkeytt� ei voida suoraan laskea samalla tavalla.

![Piirteiden t�rkeys](featureImportance.png)

## Johtop��t�kset

Analyysin perusteella voidaan tehd� seuraavat johtop��t�kset:

1. Kaikki kolme mallia suoriutuvat erinomaisesti hydrauliikkaj�rjestelm�n tilan luokittelussa, saavuttaen yli 99% tarkkuuden.
2. SVM-malli osoittautui hieman paremmaksi tarkkuuden osalta, mik� vahvistaa aiemman vertailun tulokset.
3. Random Forest ja XGBoost -mallien piirteiden t�rkeysanalyysi osoittaa, ett� pressure-muuttuja on hieman t�rke�mpi kuin pumpControl-muuttuja.
4. Mallien p��t�srajapinnat ovat selkeit�, mik� viittaa siihen, ett� luokat ovat hyvin eroteltavissa toisistaan.
5. Sekaannusmatriisit osoittavat, ett� mallit tunnistavat erityisen hyvin normal_digging-, overload- ja hose_break-tilat.

Yhteenvetona voidaan todeta, ett� SVM-malli on paras valinta hydrauliikkaj�rjestelm�n tilan luokitteluun, mutta my�s Random Forest ja XGBoost -mallit tarjoavat erinomaisen suorituskyvyn.
