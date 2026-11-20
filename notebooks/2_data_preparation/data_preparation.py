import pandas as pd
import numpy as np
from sklearn.preprocessing import RobustScaler
from sklearn.model_selection import train_test_split
from imblearn.over_sampling import SMOTE
from collections import Counter

# ==========================================
# 0. CONFIGURAÇÕES INICIAIS
# ==========================================
FILE_PATH = 'caminho_para_o_teu_dataset.csv'
TARGET = 'label'  # Nome da tua coluna alvo
SEED = 42

def load_data(filepath):
    """Carrega o dataset. Ajusta os parâmetros se for preciso (ex: sep=';')."""
    return pd.read_csv(filepath)

def main():
    # Descomenta a linha abaixo quando tiveres o ficheiro pronto no Colab
    # df = load_data(FILE_PATH)

    # --- PARA EFEITOS DE TESTE ---
    print("A gerar dados fictícios para teste do script...")
    df = pd.DataFrame(np.random.rand(1000, 10), columns=[f'feature_{i}' for i in range(10)])
    df[TARGET] = np.random.choice([0, 1], size=1000, p=[0.95, 0.05])
    # -----------------------------------------------------------

    # ==========================================
    # 1. LIMPEZA BASE (Duplicados, Nulos e Infinitos)
    # ==========================================
    print("\n--- 1. Limpeza Base ---")
    print(f"Dimensão original: {df.shape}")

    df.drop_duplicates(inplace=True)
    print(f"Após remover duplicados: {df.shape}")

    df.replace([np.inf, -np.inf], np.nan, inplace=True)
    df.dropna(inplace=True)
    print(f"Após remover nulos/infinitos: {df.shape}")

    # ==========================================
    # 2. SELEÇÃO DE FEATURES (Remover Alta Correlação)
    # ==========================================
    print("\n--- 2. Remoção de Features Colineares ---")
    numeric_cols = df.select_dtypes(include=np.number).columns.tolist()
    if TARGET in numeric_cols:
        numeric_cols.remove(TARGET)

    threshold = 0.80
    corr_matrix = df[numeric_cols].corr().abs()

    upper = corr_matrix.where(np.triu(np.ones(corr_matrix.shape), k=1).astype(bool))
    to_drop = [column for column in upper.columns if any(upper[column] >= threshold)]

    print(f"Variáveis colineares a remover ({len(to_drop)}): {to_drop}")
    df_reduced = df.drop(columns=to_drop)
    print(f"Nova dimensão: {df_reduced.shape}")

    # ==========================================
    # 3. DIVISÃO DOS DADOS (Train-Test Split)
    # ==========================================
    print("\n--- 3. Divisão dos Dados (Train/Test) ---")
    X = df_reduced.drop(columns=[TARGET])
    y = df_reduced[TARGET]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.3, random_state=SEED, stratify=y
    )
    print(f"Tamanho do Treino: {X_train.shape[0]} amostras")
    print(f"Tamanho do Teste:  {X_test.shape[0]} amostras")

    # ==========================================
    # 4. TRANSFORMAÇÃO E ESCALONAMENTO
    # ==========================================
    print("\n--- 4. Transformação e Escalonamento ---")

    skewed_features = X_train.skew().abs()
    high_skew_cols = skewed_features[skewed_features > 1.5].index.tolist()

    for col in high_skew_cols:
        if (X_train[col] >= 0).all():
            X_train.loc[:, col] = np.log1p(X_train[col])
            X_test.loc[:, col] = np.log1p(X_test[col])

    scaler = RobustScaler()
    X_train_scaled = pd.DataFrame(scaler.fit_transform(X_train), columns=X_train.columns)
    X_test_scaled = pd.DataFrame(scaler.transform(X_test), columns=X_test.columns)

    # ==========================================
    # 5. BALANCEAMENTO COM SMOTE
    # ==========================================
    print("\n--- 5. Balanceamento (SMOTE) ---")
    print(f"Distribuição ANTES do SMOTE (treino): {Counter(y_train)}")

    smote = SMOTE(random_state=SEED)
    X_train_resampled, y_train_resampled = smote.fit_resample(X_train_scaled, y_train)

    print(f"Distribuição APÓS o SMOTE (treino): {Counter(y_train_resampled)}")

    print("\n✅ Pré-processamento concluído com sucesso!")

if __name__ == "__main__":
    main()