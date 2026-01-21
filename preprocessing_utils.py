import pandas as pd
from typing import Optional, List

def manual_preprocess(df: pd.DataFrame, feature_schema: Optional[List[str]] = None) -> pd.DataFrame:
    df_prep = df.copy()

    # --- Convertir columnas SI/NO a 1/0 (idempotente) ---
    columnas_binarias = ['Sedentarismo', 'Tabaquismo', 'Antecedente Familiar']
    for col in columnas_binarias:
        if col in df_prep.columns:
            df_prep[col] = df_prep[col].replace(
                {'SI': 1, 'NO': 0, 'Si': 1, 'No': 0}
            )
            try:
                df_prep[col] = pd.to_numeric(
                    df_prep[col], errors='coerce'
                ).fillna(0).astype(int)
            except Exception:
                pass

    # --- Ajustar al esquema fijo (si existe) ---
    if feature_schema is not None:
        for col in feature_schema:
            if col not in df_prep.columns:
                df_prep[col] = 0  # columna faltante con 0
        # Mantener solo columnas del esquema y en el orden correcto
        df_prep = df_prep[feature_schema].copy()

    return df_prep


def preprocess_with_schema(X, feature_schema=None):
    """
    Wrapper pickleable para aplicar manual_preprocess con un esquema fijo.
    Esta función debe existir a nivel de módulo para que joblib la encuentre.
    """
    return manual_preprocess(X, feature_schema=feature_schema)

def preproc_fn(X, feature_schema=None):
    """Alias para compatibilidad con el pipeline guardado"""
    return manual_preprocess(X, feature_schema=feature_schema)
