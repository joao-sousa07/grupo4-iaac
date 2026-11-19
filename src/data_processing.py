import os
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler

def load_and_preprocess_data(custom_path=None, test_size=0.20, random_state=42):
    """
    Carrega o dataset de phishing, remove a coluna Index e duplicados,
    corrige o mapeamento de rótulos (1 = Phishing, 0 = Legítimo)
    e efetua a divisão estratificada com normalização.
    """
    if custom_path and os.path.exists(custom_path):
        data_path = custom_path
    else:
        possible_paths = [
            "../../data/phishing.csv",
            "../../data/raw/phishing.csv",
            "data/raw/phishing.csv",
            "data/phishing.csv",
            "../data/phishing.csv"
        ]
        data_path = next((p for p in possible_paths if os.path.exists(p)), None)

    if not data_path:
        raise FileNotFoundError("Dataset phishing.csv não foi encontrado na pasta 'data/'.")

    print(f"📊 A carregar dados de: {data_path}")
    df = pd.read_csv(data_path)

    if 'Index' in df.columns:
        df = df.drop(columns=['Index'])

    df = df.drop_duplicates()

    target_col = df.columns[-1]
    if set(df[target_col].unique()).issubset({-1, 1}):
        df[target_col] = df[target_col].map({-1: 1, 1: 0})

    X = df.drop(columns=[target_col])
    y = df[target_col]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=test_size, random_state=random_state, stratify=y
    )

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_test_scaled = scaler.transform(X_test)

    print("✅ Dados limpos, corrigidos e normalizados com sucesso.")
    return X_train_scaled, X_test_scaled, y_train, y_test, scaler, X.columns.tolist()