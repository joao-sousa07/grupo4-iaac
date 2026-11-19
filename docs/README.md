# 📚 Documentação Técnica e Funcional do Projeto

Este diretório contém a documentação técnica, os registos de desenvolvimento por Sprint e a guia de arquitetura do módulo de **Deteção de Malware** (Grupo 4 - IAAC).

---

## 🏃‍♂️ Acompanhamento de Sprints (SCRUM)

### Sprint 1: Business Understanding & Data Preparation
* **Objetivo:** Compreender o problema de negócio em Cibersegurança, realizar Análise Exploratória de Dados (EDA) e preparar o dataset para treino.
* **Tarefas Concluídas:**
  * Definição da métrica crítica de negócio (foco no Recall da classe malicious para minimizar Falsos Negativos, com o F1 da classe non-malicious como apoio).
  * EDA completa: análise univariada, correlações (Pearson e Spearman), informação mútua, PCA, t-SNE e distância de Hamming entre amostras.
  * Limpeza do dataset uci_malware_detection (remoção de 2 duplicados e 28 colunas constantes; sem valores em falta).
  * Análise de outliers (IQR e Isolation Forest), sem remover amostras, por serem características binárias.
  * Correção do mapeamento de target (1=malicious, 0=non-malicious).
  * Divisão estratificada dos dados (80% Treino / 20% Teste) e escala ajustada só no treino.
  * Comparação de 5 estratégias para dados desequilibrados (incluindo SMOTE) e exportação dos dados para data/processed/.

### Sprint 2: Model Training, Evaluation & Optimization (Módulo 7)
* **Objetivo:** Treino de modelos de Machine Learning, otimização de hiperparâmetros e avaliação técnica rigorosa.
* **Tarefas Concluídas:**
  * Engenharia de características (4 características novas e PCA) dentro de um Pipeline, para evitar data leakage.
  * Comparação de 11 modelos (Regressão Logística, Árvore de Decisão, kNN, Naive Bayes, SVM, AdaBoost, Gradient Boosting, XGBoost, Random Forest) com Stratified 5-Fold Cross-Validation.
  * Otimização de hiperparâmetros via GridSearchCV e RandomizedSearchCV, com validação cruzada aninhada.
  * Verificação e controlo de Overfitting vs. Underfitting (curvas de aprendizagem e de validação).
  * Extração e análise de Matrizes de Confusão, Curvas ROC-AUC e Precision-Recall comparativas.
  * Avaliação final no teste (Gaussian NB) com intervalo de confiança de Wilson e consolidação dos resultados para o relatório final do ISTEC.

---

## 📂 Estrutura da Documentação
* `data/`: Contém os dados brutos (raw/) e processados (processed/).
* `notebooks/`:
  * `eda_malware.ipynb`: Análise exploratória e correlação de variáveis.
  * `data_preparation_malwarev2.ipynb`: Tratamento e exportação dos datasets de treino e teste.
  * `feature_engineering_modelos.ipynb`: Engenharia de características e comparação dos modelos.
  * `model_training_and_evaluation.ipynb`: Ajuste de hiperparâmetros, avaliação e geração de gráficos.
* `reports/`': Imagens e figuras geradas pelos modelos para incorporação no relatório final.
  
---

## ⚙️ Como Executar o Projeto
1. Certifique-se de ter as dependências instaladas (`pandas`, `numpy`, `scikit-learn`, `xgboost`, `matplotlib`, `seaborn`, `scipy`, `imbalanced-learn`, `xgboost`).
2. Executar sequencialmente os notebooks na pasta notebooks/:
   1. `eda_malware.ipynb`
   2. `data_preparation_malwarev2.ipynb`
   3. `feature_engineering_modelos.ipynb`
   4. `model_training_and_evaluation.ipynb`
