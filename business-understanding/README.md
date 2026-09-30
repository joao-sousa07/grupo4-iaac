# Business & Data Understanding - Deteção de Phishing

## 🎯 Business Understanding (Entendimento de Negócio)
* **Problema:** Ataques de Phishing por meio de URLs maliciosas causam fraudes e roubo de dados.
* **Objetivo:** Criar um modelo de classificação capaz de identificar automaticamente se um URL é legítimo ou Phishing.
* **Métrica Principal:** Minimizar os Falsos Negativos (evitar que um URL malicioso seja classificado como seguro).

## 📊 Data Understanding (Entendimento dos Dados)
* **Ficheiro:** `data/phishing.csv`
* **Descrição:** Conjunto de dados contendo atributos extraídos da estrutura de URLs e páginas web para classificação de segurança.
* **Variável Target:** Classe binária indicando Phishing vs. Legítimo.
* **Ações Realizadas na EDA:**
  - Análise de valores em falta e duplicados.
  - Verificação do balanceamento de classes.
  - Análise de correlação entre variáveis e a classe alvo.