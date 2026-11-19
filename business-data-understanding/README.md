# 🛡️ Deteção de Malware: Business & Data Understanding

## 🎯 Business Understanding (Entendimento de Negócio)
* **Problema:** Programas maliciosos que passam despercebidos causam roubo de dados e perdas financeiras.
* **Objetivo:** Criar um modelo de classificação capaz de identificar automaticamente se um programa é legítimo ou Malware.
* **Métrica Principal:** Minimizar os Falsos Negativos (evitar que um programa malicioso seja classificado como seguro).

* **📊 Data Understanding (Entendimento dos Dados)
* **Ficheiro:** `data/uci_malware_detection.csv`
* **Descrição:** Conjunto de dados contendo 531 características binárias (0/1) que descrevem o comportamento de 373 programas.
* **Variável Target:** Classe binária indicando Malware (malicious) vs. Legítimo (non-malicious).
* **Ações Realizadas na EDA:**
  - Análise de valores em falta e duplicados.
  - Verificação do balanceamento de classes.
  - Análise de correlação entre variáveis e a classe alvo.
