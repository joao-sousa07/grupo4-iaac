# Data Understanding — Projeto IAAC

## 1. Origem dos dados

Foi utilizado o dataset *IoT Malware Network Traffic Dataset (CIC-YNU-2026)*, disponibilizado na plataforma Kaggle.

O dataset contém registos de tráfego de rede IoT, utilizados para estudar padrões associados a diferentes famílias de malware.

## 2. Estrutura dos dados

O conjunto de dados original utilizado no projeto contém aproximadamente 737 mil registos e 42 colunas.

Entre as variáveis analisadas encontram-se características relacionadas com protocolos, flags TCP, contagens e estatísticas do tráfego de rede.

## 3. Variável de classificação

A variável `MalwareFamily` identifica a classe associada a cada registo.

Entre as classes presentes nos testes encontram-se:

- Benign
- Mirai
- DarkNexus
- Generic
- Tsunami
- Unknown

## 4. Análise inicial

Durante a exploração dos dados, foram considerados aspetos como a distribuição das classes, a qualidade dos valores e a adequação das características ao treino dos modelos.

O desequilíbrio entre classes é um aspeto importante, porque pode afetar a capacidade do modelo para identificar famílias menos representadas.

## 5. Preparação posterior

Após a compreensão inicial dos dados, foram aplicadas operações de preparação e pré-processamento para permitir o treino e a avaliação dos algoritmos.

O pipeline guardado utiliza transformações de características, tratamento de valores em falta e normalização.

## 6. Importância desta fase

O Data Understanding permitiu compreender a informação disponível, identificar possíveis limitações e apoiar as decisões tomadas durante a preparação dos dados e a modelação.