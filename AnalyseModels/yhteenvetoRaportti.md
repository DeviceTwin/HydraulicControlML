# Hydrauliikkajärjestelmän tilojen tunnistus - Mallien analyysi

## Yhteenveto

Tässä raportissa analysoidaan kolmen koneoppimismallin suorituskykyä hydrauliikkajärjestelmän tilojen tunnistuksessa.
Mallit ovat Support Vector Machine (SVM), Random Forest ja XGBoost.

## Mallien suorituskyky

| Malli | Tarkkuus | Precision | Recall | F1-Score |
|-------|----------|-----------|--------|----------|
| SVM | 0.9906 | 0.9872 | 0.9896 | 0.9883 |
| Random Forest | 0.9913 | 0.9876 | 0.9908 | 0.9890 |
| XGBoost | 0.9906 | 0.9878 | 0.9889 | 0.9883 |

## Analyysi

### Päätösrajapinnat

Päätösrajapintakuvaajat näyttävät, miten mallit luokittelevat syöteavaruuden. Tämä auttaa ymmärtämään mallien päätöksentekoprosessia.

![Päätösrajapinnat](decisionBoundaries.png)

### Sekaannusmatriisit

Sekaannusmatriisit näyttävät, miten mallit ennustavat eri luokkia. Diagonaalilla olevat arvot ovat oikeita ennusteita, ja muut arvot ovat virheellisiä ennusteita.

![Sekaannusmatriisit](confusionMatrices.png)

### Piirteiden tärkeys

Piirteiden tärkeysvertailu näyttää, mitkä syötemuuttujat ovat tärkeimpiä mallien päätöksenteossa.

![Piirteiden tärkeys](featureImportance.png)

### ROC-käyrät

ROC-käyrät (Receiver Operating Characteristic) näyttävät mallien suorituskyvyn eri kynnysarvoilla. Käyrän alla oleva pinta-ala (AUC) kuvaa mallin erottelukykyä.

![ROC-käyrät](rocCurves.png)

### Precision-Recall -käyrät

Precision-Recall -käyrät näyttävät tarkkuuden ja saannin välisen suhteen eri kynnysarvoilla. Tämä on hyödyllistä erityisesti epätasapainoisissa luokittelutehtävissä.

![Precision-Recall -käyrät](precisionRecallCurves.png)

## Johtopäätökset

Analyysin perusteella voidaan todeta, että kaikki kolme mallia suoriutuvat hyvin hydrauliikkajärjestelmän tilojen tunnistuksessa. 
Mallien välillä on kuitenkin pieniä eroja suorituskyvyssä ja ominaisuuksissa:

1. **SVM**: Yksinkertainen ja tehokas malli, mutta ei tue todennäköisyysennusteita.
2. **Random Forest**: Hyvä yleinen suorituskyky ja tukee todennäköisyysennusteita.
3. **XGBoost**: Korkein tarkkuus ja tukee todennäköisyysennusteita.

### Mallien käyttökelpoisuus tuotannossa

Kaikki kolme mallia (SVM, Random Forest ja XGBoost) ovat erittäin käyttökelpoisia tuotannossa:

1. **SVM**:
   - Erinomainen tarkkuus (99.06%)
   - Yksinkertaisin malli, mikä voi olla etu resurssirajoitteisissa ympäristöissä
   - Rajoitteena todennäköisyysennusteiden puuttuminen

2. **Random Forest**:
   - Paras kokonaistarkkuus (99.13%)
   - Tukee todennäköisyysennusteita
   - Hyvä tasapaino tarkkuuden ja monimutkaisuuden välillä

3. **XGBoost**:
   - Erinomainen tarkkuus (99.06%)
   - Tukee todennäköisyysennusteita
   - Hieman monimutkaisempi kuin muut mallit

Mallien välillä ei ole merkittäviä eroja suorituskyvyssä, joten valinta voi perustua muihin tekijöihin:

- Jos tarvitset todennäköisyysennusteita, valitse Random Forest tai XGBoost
- Jos haluat yksinkertaisimman mallin, valitse SVM
- Jos haluat parhaan kokonaistarkkuuden, valitse Random Forest

Kaikki mallit ovat valmiita tuotantokäyttöön, eikä niissä ole havaittavissa merkittäviä virheitä tai ylikoulutusta.
