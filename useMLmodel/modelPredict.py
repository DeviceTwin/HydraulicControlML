import pandas as pd
import numpy as np
import os
import pickle
import joblib
import sys
from sklearn.preprocessing import LabelEncoder

# Määritä tiedostojen nimet
MODEL_FILENAME = "SVM.pkl"
SCALER_FILENAME = "hydraulicScaler.joblib"

def loadModelAndScaler():
    """
    Lataa SVM-malli ja skaalauskomponentti
    
    Returns:
        model: Ladattu SVM-malli
        scaler: Ladattu skaalauskomponentti
        labelEncoder: Ladattu luokkien koodaaja
    """
    try:
        currentDir = os.path.dirname(os.path.abspath(__file__))
        projectRoot = os.path.dirname(currentDir)
        modelsDir = os.path.join(projectRoot, 'Models')
        
        # Lataa SVM-malli
        modelPath = os.path.join(modelsDir, MODEL_FILENAME)
        with open(modelPath, 'rb') as f:
            model = pickle.load(f)
        
        # Lataa skaalauskomponentti
        scalerPath = os.path.join(modelsDir, SCALER_FILENAME)
        scaler = joblib.load(scalerPath)
        
        # Luo ja alusta LabelEncoder luokkien koodaamiseen
        labelEncoder = LabelEncoder()
        labelEncoder.fit(['hose_break', 'normal_digging', 'normal_empty', 'normal_full', 'overload'])
        
        return model, scaler, labelEncoder
    except Exception as e:
        print(f"Virhe mallin tai skaalerin lataamisessa: {e}")
        sys.exit(1)

def predictState(pumpControl, pressure):
    """
    Ennustaa hydrauliikkajärjestelmän tilan annettujen arvojen perusteella
    
    Args:
        pumpControl: Pumpun ohjausarvo (18-101)
        pressure: Painearvo (1-432)
        
    Returns:
        state: Ennustettu tila (normal_digging, normal_full, normal_empty, overload, hose_break)
    """
    try:
        # Tarkista että arvot ovat sallitulla alueella
        if pumpControl < 18 or pumpControl > 101:
            print(f"Varoitus: pumpControl arvo {pumpControl} on sallitun alueen [18, 101] ulkopuolella")
        
        if pressure < 1 or pressure > 432:
            print(f"Varoitus: pressure arvo {pressure} on sallitun alueen [1, 432] ulkopuolella")
        
        # Lataa malli, skaaleri ja labelEncoder
        model, scaler, labelEncoder = loadModelAndScaler()
        
        # Skaalaa arvot manuaalisesti välille [0, 1]
        # pumpControl: [18, 101] -> [0, 1]
        # pressure: [1, 432] -> [0, 1]
        pumpControlScaled = (pumpControl - 18) / (101 - 18)
        pressureScaled = (pressure - 1) / (432 - 1)
        
        # Varmista että skaalatut arvot ovat välillä [0, 1]
        pumpControlScaled = max(0, min(1, pumpControlScaled))
        pressureScaled = max(0, min(1, pressureScaled))
        
        # Luo DataFrame skaalatulla datalla
        scaledInput = pd.DataFrame({
            'pumpControl': [pumpControlScaled], 
            'pressure': [pressureScaled]
        })
        
        # Tee ennuste
        prediction = model.predict(scaledInput)[0]
        
        # Muunna numeerinen ennuste tekstiksi käyttäen labelEncoder-luokkaa
        predictedState = labelEncoder.inverse_transform([prediction])[0]
        
        # Tulosta debug-tietoja
        print(f"\nSyötetyt arvot: pumpControl={pumpControl}, pressure={pressure}")
        print(f"Skaalatut arvot: pumpControl={pumpControlScaled:.6f}, pressure={pressureScaled:.6f}")
        print(f"Numeerinen ennuste: {prediction}")
        print(f"Tekstimuotoinen ennuste: {predictedState}")
        
        return predictedState
    except Exception as e:
        print(f"Virhe ennustettaessa: {e}")
        return "error"

def main():
    """
    Pääfunktio, joka kysyy käyttäjältä syötearvot ja tulostaa ennustetun tilan
    """
    print("Hydrauliikkajärjestelmän tilan ennustus")
    print("="*40)
    
    try:
        # Kysy käyttäjältä syötearvot
        pumpControl = float(input("Syötä pumpControl-arvo (18-101): "))
        pressure = float(input("Syötä pressure-arvo (1-432): "))
        
        # Ennusta tila
        state = predictState(pumpControl, pressure)
        
        # Tulosta ennustettu tila
        print(f"\nEnnustettu tila: {state}")
        
    except ValueError:
        print("Virhe: Syötä kelvollinen numeroarvo.")
    except Exception as e:
        print(f"Virhe: {str(e)}")

if __name__ == "__main__":
    main()