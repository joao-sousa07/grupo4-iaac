# Business Understanding — Projeto IAAC

## 1. Problema

Os dispositivos IoT, como câmaras de segurança, sensores e routers, podem ser utilizados como alvos de ataques informáticos. A análise manual de grandes quantidades de tráfego de rede é difícil e demorada.

## 2. Objetivo

O objetivo do projeto é desenvolver uma solução baseada em Inteligência Artificial que permita classificar tráfego de rede IoT e identificar possíveis famílias de malware.

## 3. Solução proposta

O sistema utiliza um algoritmo de Machine Learning supervisionado, o Random Forest, para classificar o tráfego.

Foi também integrado o Llama 3.2, através do Ollama, para gerar explicações sobre os resultados, os possíveis riscos e as medidas de proteção.

## 4. Critérios de sucesso

- Preparar os dados para utilização nos modelos.
- Treinar e comparar diferentes algoritmos.
- Avaliar o desempenho através de métricas como accuracy, precision, recall e F1-score.
- Integrar uma IA generativa para explicar os resultados.
- Testar o funcionamento da solução e gerar relatórios automáticos.

## 5. Limitações

O sistema é um protótipo académico e não substitui uma solução profissional de deteção de intrusões.

As classificações podem conter erros e as explicações produzidas pela IA generativa devem ser verificadas.