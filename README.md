# Grupo 4 — IAAC

## 1. Descrição do projeto

Este projeto foi desenvolvido no âmbito da unidade curricular de Inteligência Artificial Aplicada à Cibersegurança (IAAC).

O objetivo é aplicar técnicas de Machine Learning à análise de dados relacionados com cibersegurança, com especial atenção à classificação de tráfego de rede IoT e à identificação de famílias de malware.

O projeto segue uma organização modular, separando dados, notebooks, código-fonte, modelos, documentação, relatórios e testes.

## 2. Objetivos

- Compreender e explorar os dados utilizados.
- Preparar os dados para o treino de modelos.
- Aplicar algoritmos de Machine Learning supervisionado.
- Comparar os modelos utilizando métricas de avaliação.
- Identificar possíveis famílias de malware.
- Integrar IA generativa para explicar os resultados.
- Documentar e testar a solução desenvolvida.

## 3. Dataset

Na componente de classificação de tráfego IoT foi utilizado o dataset **IoT Malware Network Traffic Dataset (CIC-YNU-2026)**, disponível no Kaggle.

Link: https://www.kaggle.com/datasets/raneemababneh/iot-malware-network-traffic-dataset-cic-ynu-2026

O dataset contém características de tráfego de rede e uma variável de classificação denominada `MalwareFamily`.

## 4. Tecnologias utilizadas

- Python
- Pandas e NumPy
- Scikit-learn
- XGBoost
- Jupyter Notebook
- Random Forest
- Llama 3.2
- Ollama
- Git e GitHub

## 5. Modelos de Machine Learning

Foram comparados diferentes algoritmos de classificação:

- Logistic Regression
- Decision Tree
- Random Forest
- XGBoost

O Random Forest foi selecionado para uma avaliação mais aprofundada.

Na avaliação final do Random Forest otimizado, foram obtidos os seguintes resultados:

| Métrica | Resultado |
|---|---|
| Amostras de teste | 59 004 |
| Accuracy | 50,25% |
| Precision macro | 38,37% |
| Recall macro | 52,94% |
| F1-score macro | 38,63% |

Estes resultados correspondem ao modelo otimizado da avaliação final, não necessariamente ao ficheiro `models/random_forest.pkl` utilizado na integração.

## 6. Integração de IA generativa

Foi desenvolvida uma integração entre um modelo Random Forest e o Llama 3.2, executado localmente através do Ollama.

O funcionamento é o seguinte:

1. O sistema seleciona uma amostra do dataset.
2. O Random Forest prevê a classe do tráfego.
3. A previsão é enviada ao Llama 3.2.
4. O Llama gera uma explicação sobre a classificação, os possíveis riscos e as medidas de proteção.
5. O resultado é guardado automaticamente num relatório TXT.

A IA generativa não realiza a classificação do tráfego. A sua função é explicar a previsão do modelo de Machine Learning.

## 7. Estrutura do repositório

- `business-data-understanding/` — definição do problema e compreensão dos dados.
- `data/` — dados brutos e processados.
- `docs/` — documentação do projeto.
- `ia_generativa/` — integração do Random Forest com o Llama 3.2.
- `models/` — modelos treinados.
- `notebooks/` — preparação, exploração, engenharia de características, treino e avaliação.
- `references/` — referências e materiais de apoio.
- `reports/` — resultados, gráficos e relatórios de análise.
- `src/` — código-fonte do projeto.
- `tests/` — testes de classificação e da integração com IA generativa.

## 8. Execução da integração

É necessário ter Python, as dependências do projeto e o Ollama instalado, com o modelo `llama3.2` disponível localmente.

Instalar as dependências:

```powershell
python -m pip install -r requirements.txt
python -m pip install requests kagglehub joblib
```

Descarregar o modelo generativo:

```powershell
ollama pull llama3.2
```

Executar a integração:

```powershell
python .\ia_generativa\integrar_modelos.py
```

O programa necessita do modelo treinado em `models/random_forest.pkl`, que não deve ser incluído diretamente no GitHub devido ao seu tamanho.

## 9. Testes

Executar os testes da integração generativa:

```powershell
python .\tests\teste_ia_generativa.py
```

Executar o teste exploratório de classificação:

```powershell
python .\tests\teste_classificacao.py
```

Foram realizados cinco testes automatizados de integração com respostas simuladas do Ollama, todos concluídos com sucesso.

O teste exploratório com 20 amostras obteve 25% de accuracy. Este valor não substitui a avaliação final em dados de teste independentes.

## 10. Limitações

A classificação automática pode apresentar erros, incluindo a identificação de tráfego malicioso como benigno.

O Llama 3.2 pode produzir explicações imprecisas, pelo que os resultados devem ser verificados.

O sistema foi desenvolvido para fins académicos e não substitui uma solução profissional de deteção de ameaças.

## 11. Grupo 4

Projeto desenvolvido no âmbito da unidade curricular IAAC.

Os elementos do grupo, respetivas responsabilidades e registos de sprints/SCRUM devem constar da documentação final.