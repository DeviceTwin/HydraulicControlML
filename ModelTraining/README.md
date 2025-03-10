# ModelTraining

Tämä hakemisto sisältää koneoppimismallien koulutukseen ja arviointiin liittyvät Jupyter Notebookit ja dokumentaation.

## Jupyter Notebookit

### 1. modelTraining.ipynb
- Mallien koulutus ja arviointi
  * Support Vector Machine (SVM)
  * Random Forest
  * XGBoost
- Mallien suorituskyvyn arviointi
  * Tarkkuus (Accuracy)
  * Sekaannusmatriisit (Confusion Matrices)
  * Oppimiskäyrät (Learning Curves)
- Hyperparametrien vaikutusten analysointi
  * SVM: C-parametrin vaikutus
  * Random Forest: n_estimators-parametrin vaikutus
  * XGBoost: max_depth-parametrin vaikutus
- Tallentaa:
  * `../Models/svmModel.joblib`
  * `../Models/rfModel.joblib`
  * `../Models/xgbModel.joblib`
  * `../Visualization/learningCurves.png`
  * `../Visualization/hyperparameterEffects.png`
  * `../Visualization/model_comparisons.png`

## Visualisoinnit

### 1. Mallien oppimiskäyrät
- Oppimiskäyrät näyttävät, miten koulutusdatan koko vaikuttaa mallien tarkkuuteen
- Visualisointi auttaa tunnistamaan mahdolliset ylisovittamisen (overfitting) tai alisovittamisen (underfitting) ongelmat

### 2. Hyperparametrien vaikutukset
- SVM: C-parametrin vaikutus mallin tarkkuuteen
- Random Forest: Estimaattoreiden määrän vaikutus mallin tarkkuuteen
- XGBoost: Puun maksimisyvyyden vaikutus mallin tarkkuuteen

### 3. Mallien vertailu
- Sekaannusmatriisit kaikille malleille
- Mallien tarkkuuksien vertailu pylväsdiagrammina
- Visualisointi auttaa valitsemaan parhaan mallin käyttötarkoitukseen

## Käyttö

1. Asenna tarvittavat kirjastot:
```bash
pip install pandas numpy matplotlib seaborn scikit-learn xgboost
```

2. Avaa Jupyter Notebook:
```bash
jupyter notebook modelTraining.ipynb
```

3. Suorita solut järjestyksessä mallien kouluttamiseksi ja arvioimiseksi

## Tulokset

Mallien vertailu osoittaa, että SVM-malli suoriutuu parhaiten hydraulisen järjestelmän tilan luokittelussa:

1. **SVM**:
   - Tarkkuus: 99.33%
   - Optimaaliset hyperparametrit: C=100, gamma='scale', kernel='rbf'

2. **Random Forest**:
   - Tarkkuus: 99.13%
   - Optimaaliset hyperparametrit: n_estimators=100, max_depth=None

3. **XGBoost**:
   - Tarkkuus: 98.93%
   - Optimaaliset hyperparametrit: max_depth=5, learning_rate=0.1

Ominaisuuksien tärkeydessä pressure (0.56) oli hieman tärkeämpi kuin pumpControl (0.44).
