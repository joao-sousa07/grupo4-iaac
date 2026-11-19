
from pathlib import Path
from datetime import datetime

import glob
import joblib
import kagglehub
import numpy as np
import pandas as pd

from explicar_ameaca import explicar_ameaca


BASE = Path(__file__).resolve().parent.parent
MODELO_PATH = BASE / "models" / "random_forest.pkl"
PASTA_RELATORIOS = BASE / "reports" / "analises_ia"

DATASET = (
    "raneemababneh/"
    "iot-malware-network-traffic-dataset-cic-ynu-2026"
)


def carregar_modelo():
    if not MODELO_PATH.exists():
        raise FileNotFoundError(
            f"Modelo não encontrado: {MODELO_PATH}"
        )

    modelo = joblib.load(MODELO_PATH)

    if not hasattr(modelo, "predict"):
        raise ValueError("O ficheiro não contém um modelo válido.")

    return modelo


def obter_amostra(modelo):
    pasta = kagglehub.dataset_download(DATASET)
    ficheiros = sorted(
        glob.glob(str(Path(pasta) / "**" / "*.csv"), recursive=True)
    )

    if not ficheiros:
        raise FileNotFoundError("Dataset CSV não encontrado.")

    colunas = list(modelo.feature_names_in_)

    # Ler por blocos para reduzir o consumo de memória.
    for bloco in pd.read_csv(ficheiros[0], chunksize=10000):
        if "MalwareFamily" not in bloco.columns:
            raise ValueError("Coluna MalwareFamily não encontrada.")

        em_falta = [c for c in colunas if c not in bloco.columns]
        if em_falta:
            raise ValueError(f"Colunas em falta: {em_falta}")

        maliciosos = bloco[
            bloco["MalwareFamily"]
            .astype(str)
            .str.lower()
            .ne("benign")
        ]

        if not maliciosos.empty:
            original = maliciosos.iloc[[0]]
            classe_real = str(original["MalwareFamily"].iloc[0])

            amostra = original[colunas].copy()
            amostra = amostra.replace(
                [np.inf, -np.inf], np.nan
            )

            return amostra, classe_real

    raise ValueError("Não foram encontradas amostras maliciosas.")


def guardar_relatorio(classe_real, previsao, explicacao):
    PASTA_RELATORIOS.mkdir(parents=True, exist_ok=True)

    agora = datetime.now()
    nome = agora.strftime("analise_%Y%m%d_%H%M%S_%f.txt")
    destino = PASTA_RELATORIOS / nome

    conteudo = f"""RELATÓRIO DE ANÁLISE DE TRÁFEGO IoT

Data: {agora.strftime("%d/%m/%Y %H:%M:%S")}

Modelo de classificação: Random Forest
Classe real: {classe_real}
Classe prevista: {previsao}

Modelo de IA generativa: Llama 3.2 (Ollama)

EXPLICAÇÃO DA IA:
{explicacao}

NOTA:
A previsão automática não confirma uma infeção.
As explicações da IA devem ser verificadas.
"""

    destino.write_text(conteudo, encoding="utf-8")
    return destino


def main():
    print("A carregar o Random Forest...")
    modelo = carregar_modelo()

    print("A procurar uma amostra real...")
    amostra, classe_real = obter_amostra(modelo)

    previsao = str(modelo.predict(amostra)[0])

    print("\nClasse real:", classe_real)
    print("Família prevista:", previsao)

    print("\nA gerar explicação com Llama 3.2...")
    explicacao = explicar_ameaca(previsao)

    print("\nEXPLICAÇÃO DA IA:")
    print(explicacao)

    destino = guardar_relatorio(
        classe_real, previsao, explicacao
    )

    print("\nRelatório guardado em:", destino)


if __name__ == "__main__":
    try:
        main()
    except Exception as erro:
        print(f"\nErro na análise: {erro}")
