import pandas as pd
from sklearn.preprocessing import LabelEncoder

def manual_preprocess(df: pd.DataFrame) -> pd.DataFrame:
    df_prep = df.copy()

    # --- Convertir columnas SI/NO a 1/0 ---
    columnas_binarias = ['Sedentarismo','Tabaquismo','Antecedente Familiar']
    for col in columnas_binarias:
        df_prep[col] = df_prep[col].map({'SI': 1, 'NO': 0})

    # --- Label encoding para categóricas ---
    categoricas = ['Estrato','tipo_vinculacion','ocupacion_validada']
    for col in categoricas:
        le = LabelEncoder()
        df_prep[col] = le.fit_transform(df_prep[col].astype(str))

    return df_prep