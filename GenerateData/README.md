# Hydraulisen järjestelmän datan generointi ja sen analyysi

Tämä kansio sisältää Jupyter Notebook -toteutuksen hydraulisen järjestelmän datan generointiin ja visualisointiin. Notebook on suunniteltu tuottamaan realistista dataa hydraulisen järjestelmän eri toimintatiloista koneoppimisen kehitystä varten.

## Pääkomponentti: GenerateData.ipynb

Jupyter Notebook sisältää kaikki tarvittavat toiminnallisuudet:

### 1. Datan generointi

- **Normaalit toimintatilat:**
  - Tyhjän kauhan liikkeet (nosto, lasku, siirto)
  - Normaali kaivuu (maahan tunkeutuminen, täyttö, nosto, tyhjennys)
  - Täyden kauhan liikkeet (nosto, siirto, lasku)

- **Vikatilat:**
  - Ylikuormitustilanteet (30% datasta)
  - Letkurikot (10% datasta)

- **Datan ominaisuudet:**
  - Pumpun ohjaus (0-100%)
  - Paine (0-450 bar)
  - Tila (normal_empty, normal_digging, normal_full, overload, hose_break)

### 2. Visualisointi ja analyysi

Notebook tuottaa seuraavat visualisoinnit:

1. **Scatter plot:** Pumpun ohjauksen ja paineen suhde eri tiloissa
2. **Pie chart:** Tilojen jakauma datassa
3. **Density plot:** Pumpun ohjauksen jakauma tiloittain
4. **Density plot:** Paineen jakauma tiloittain

## Kansiorakenne

- `Data/`: Generoitu CSV-tiedosto (hydraulic_data.csv)
- `Analysis/`: Visualisoinnit (hydraulic_analysis.png)
- `GenerateData/`: Jupyter Notebook ja dokumentaatio

## Käyttö

1. Käynnistä Jupyter Notebook:
   ```bash
   jupyter notebook GenerateData.ipynb
   ```

2. Suorita solut järjestyksessä:
   - Kirjastojen tuonti
   - Datan generointi
   - Visualisointi ja analyysi

3. Tulokset:
   - CSV-tiedosto tallentuu `Data`-kansioon
   - Visualisoinnit tallentuvat `Analysis`-kansioon
