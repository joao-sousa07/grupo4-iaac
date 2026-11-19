# 📚 Documentação Técnica e Funcional do Projeto

Este diretório contém a documentação técnica, os registos de desenvolvimento por Sprint e a guia de arquitetura do projeto de **Deteção de Phishing URLs** (Grupo 4 - IAAC).

---

## 🏃‍♂️ Acompanhamento de Sprints (SCRUM)

### Sprint 1: Business Understanding & Data Preparation
* **Objetivo:** Compreender o problema de negócio em Cibersegurança, realizar Análise Exploratória de Dados (EDA) e preparar os datasets para treino.
* **Tarefas Concluídas:**
  * Definição da métrica crítica de negócio (foco no **Recall** para minimizar Falsos Negativos).
  * Limpeza do dataset UCI Phishing Websites (remoção da coluna `Index` e eliminação de 47% de duplicados).
  * Correção do mapeamento de target ($1 = \text{Phishing}$, $0 = \text{Legítimo}$).
  * Normalização e divisão estratificada dos dados (80% Treino / 20% Teste).

### Sprint 2: Model Training, Evaluation & Optimization (Módulo 7)
* **Objetivo:** Treino de modelos de Machine Learning (Random Forest, XGBoost, SVM), otimização de hiperparâmetros e avaliação técnica rigorosa.
* **Tarefas Concluídas:**
  * Otimização do **Random Forest** via `GridSearchCV` com *Stratified 5-Fold Cross-Validation*.
  * Verificação e controlo de *Overfitting* vs. *Underfitting* em treino e teste.
  * Extração e análise de Matrizes de Confusão e Curvas ROC-AUC comparativas.
  * Consolidação dos resultados para o relatório final do ISTEC.

---

## 📂 Estrutura da Documentação

* `data/`: Contém os dados brutos (`raw/`) e processados (`processed/`).
* `notebooks/`:
  * `1_exploratory_data_analysis/eda.ipynb`: Análise exploratória e correlação de variáveis.
  * `2_data_preparation/data.ipynb`: Tratamento e exportação dos datasets de treino e teste.
  * `4_model_training_and_evaluation/model_training.ipynb`: Treino, ajuste de hiperparâmetros (Módulo 7) e geração de gráficos de avaliação.
* `reports/`: Imagens e figuras geradas pelos modelos para incorporação no relatório final.

---

## ⚙️ Como Executar o Projeto

1. Certifique-se de ter as dependências instaladas (`pandas`, `numpy`, `scikit-learn`, `xgboost`, `matplotlib`, `seaborn`).
2. Executar sequencialmente os notebooks na pasta `notebooks/`:
   1. `eda.ipynb`
   2. `data.ipynb`
   3. `model_training.ipynb`