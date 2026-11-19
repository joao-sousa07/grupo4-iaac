
from pathlib import Path
import glob

import joblib
import kagglehub
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score, classification_report

BASE = Path(__file__).resolve().parent.parent
MODELO = BASE / "models" / "random_forest.pkl"

DATASET = (
    "raneemababneh/"
    "iot-malware-network-traffic-dataset-cic-ynu-2026"
)

# Carregar o modelo guardado
modelo = joblib.load(MODELO)
colunas = list(modelo.feature_names_in_)

print("Random Forest carregado.")

# Obter o dataset
pasta = kagglehub.dataset_download(DATASET)
ficheiros = sorted(
    glob.glob(str(Path(pasta) / "**" / "*.csv"), recursive=True)
)

if not ficheiros:
    raise FileNotFoundError("Dataset CSV não encontrado.")

# Procurar até 4 amostras de cada classe
amostras = {}
MAX_POR_CLASSE = 4

for bloco in pd.read_csv(ficheiros[0], chunksize=10000):
    for familia, grupo in bloco.groupby("MalwareFamily"):
        if pd.isna(familia):
            continue

        familia = str(familia)

        if len(amostras.get(familia, [])) >= MAX_POR_CLASSE:
            continue

        restantes = MAX_POR_CLASSE - len(
            amostras.get(familia, [])
        )

        novas = grupo.head(restantes).to_dict("records")
        amostras.setdefault(familia, []).extend(novas)

    # Parar quando tivermos 5 classes com 4 amostras
    completas = sum(
        len(linhas) >= MAX_POR_CLASSE
        for linhas in amostras.values()
    )

    if completas >= 5:
        break

# Selecionar 5 classes e até 4 amostras de cada
classes = sorted(amostras)[:5]

linhas = []
for familia in classes:
    linhas.extend(amostras[familia][:MAX_POR_CLASSE])

dados = pd.DataFrame(linhas)

if dados.empty:
    raise ValueError("Não foram encontradas amostras.")

X = dados[colunas].replace([np.inf, -np.inf], np.nan)
y_real = dados["MalwareFamily"].astype(str)

# Fazer previsões
y_previsto = modelo.predict(X)

resultados = pd.DataFrame({
    "Classe real": y_real.to_numpy(),
    "Previsao": y_previsto
})

resultados["Correto"] = (
    resultados["Classe real"] == resultados["Previsao"]
)

print("\nRESULTADOS DOS TESTES")
print(resultados.to_string(index=False))

print("\nAccuracy:", round(
    accuracy_score(y_real, y_previsto) * 100, 2
), "%")

print("\nRELATORIO POR CLASSE")
print(classification_report(
    y_real, y_previsto, zero_division=0
))

# Guardar os resultados
destino = BASE / "reports" / "testes_ia"
destino.mkdir(parents=True, exist_ok=True)

resultados.to_csv(
    destino / "resultados_20_amostras.csv",
    index=False,
    encoding="utf-8-sig"
)

print("\nResultados guardados em:", destino)

