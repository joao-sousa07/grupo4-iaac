# Projeto de Cibersegurança e Machine Learning - Grupo 4

## 📌 Descrição Geral
Este repositório reúne os desenvolvimentos em Machine Learning aplicados à cibersegurança e deteção de ameaças. O projeto está estruturado em *branches* individuais, onde cada membro trabalha sobre um conjunto de dados específico direcionado a um problema de segurança.

## 👥 Elementos do Grupo, Branches e Datasets
* **João Sousa**
  * **Dataset:** [IoT Malware Network Traffic Dataset (CIC-YNU-2026)](https://www.kaggle.com/datasets/raneemababneh/iot-malware-network-traffic-dataset-cic-ynu-2026)
  * **Foco:** Análise e deteção de tráfego de rede malicioso em dispositivos IoT.
* **Gonçalo**
  * **Dataset:** [IoT Intrusion Detection Dataset](https://www.kaggle.com/datasets/rahult25/iot-intrusion-detection-dataset)
  * **Foco:** Deteção de intrusões e anomalias de segurança em redes IoT.
* **Margarida**
  * **Dataset:** [Malware Executable Detection](https://www.kaggle.com/datasets/piyushrumao/malware-executable-detection/data)
  * **Foco:** Classificação e deteção de ficheiros executáveis maliciosos (Malware).
* **Rafael Costa**
  * **Dataset:** Deteção de Phishing URLs (`phishing.csv`)
  * **Foco:** Classificação de URLs legítimos vs. Phishing para mitigação de fraudes.

---

## 📁 Estrutura do Repositório
```text
grupo4-iaac/
├── data/                       # Datasets brutos e processados (X_train, X_test, etc.)
├── docs/                       # Relatórios de Sprint (Sprint_2.md)
├── notebooks/                  # Notebooks sequenciais do projeto
│   ├── 1_data_preparation/     # Limpeza, nulos, duplicados e split 80/20
│   ├── 2_exploratory_data_analysis/ # EDA e Business/Data Understanding
│   ├── 3_feature_engineering/  # Normalização, seleção de atributos e SMOTE
│   └── 4_model_training_and_evaluation/ # Treino de modelos e avaliação de métricas
└── reports/                    # Gráficos e matrizes de confusão gerados