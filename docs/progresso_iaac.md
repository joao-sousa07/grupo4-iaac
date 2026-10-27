# Estado do projeto IAAC — 27/10/2026

Dataset: [IoT Malware Network Traffic Dataset (CIC-YNU-2026)](https://www.kaggle.com/datasets/raneemababneh/iot-malware-network-traffic-dataset-cic-ynu-2026). A orientação do projeto é usar a fonte Kaggle, não versionar o dataset completo no repositório.

## Trabalho realizado
- **Business and Data Understanding:** EDA com distribuição de classes, histogramas, correlações e análise de outliers (conforme gráficos partilhados).
- **Data Preparation:** existe notebook de preparação e tratamento de dados; requer revisão/reprodução integral antes da entrega.
- **Supervised Learning:** experiências com Random Forest inicial, ajustado, baixo RAM e Extra Trees baixo RAM.
- **Model Evaluation & Optimization:** pesquisa limitada de cinco configurações e avaliação do Random Forest otimizado na validação completa. Resultados em [avaliacao_random_forest.md](avaliacao_random_forest.md).

## Estado
O candidato atual é o Random Forest otimizado com F1 macro **0.3931** e accuracy **0.5940** na validação completa. Isto **não** equivale a avaliação final em teste independente. Classe `Other_rare` permanece com recall de **0.0000**.

## Próximos passos
- Garantir separação adequada de treino/validação/teste, especialmente por Hash ou outras identidades de fluxo.
- Validar pipeline de pré-processamento e verificar se o treino foi feito sem informação do conjunto de validação.
- Executar avaliação final somente depois de fixar o candidato.
- Registar métricas finais e comparar classes minoritárias.
- Atualizar documentação de execução do Colab e dependências.

Esta documentação resume resultados observados, sem afirmar que o notebook ou o modelo foram reproduzidos nesta sessão.
