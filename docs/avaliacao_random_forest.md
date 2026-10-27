# Avaliação e otimização do Random Forest

## Objetivo
Classificar tráfego IoT nas classes Benign, DarkNexus, Generic, Mirai, Other_rare e Unknown. Resultados obtidos em validação, não em teste final independente.

## Comparação dos modelos (validação)

| Modelo | Accuracy | Precision macro | Recall macro | F1 macro | F1 weighted |
|---|---:|---:|---:|---:|---:|
| Random Forest inicial | 0.7155 | 0.3849 | 0.3016 | 0.3072 | 0.6990 |
| Random Forest ajustado | 0.5686 | 0.4000 | 0.4785 | 0.3897 | 0.6298 |
| Random Forest baixo RAM | 0.4297 | 0.3841 | 0.4941 | 0.3585 | 0.5012 |
| Extra Trees baixo RAM | 0.4275 | 0.3916 | 0.4808 | 0.3554 | 0.5016 |
| Random Forest otimizado | 0.5940 | 0.3936 | 0.4690 | **0.3931** | 0.6487 |

O Random Forest otimizado teve o F1 macro mais alto observado na validação completa, mas a melhoria face ao ajustado (0.0034) é pequena e o recall macro desceu.

## Pesquisa controlada
Cinco combinações de hiperparâmetros foram avaliadas numa amostra de 100 000 exemplos de treino e 30 000 de validação. Melhor configuração na amostra: F1 macro = 0.3943.

```json
{
  "n_estimators": 100,
  "max_depth": 24,
  "min_samples_split": 10,
  "min_samples_leaf": 1,
  "max_features": "sqrt",
  "class_weight": "balanced"
}
```

O candidato foi posteriormente avaliado na validação completa (80 101 registos), com F1 macro de 0.3931. Foi treinado na amostra de 100 000 exemplos e não necessariamente no conjunto de treino integral.

## Relatório por classe — Random Forest otimizado

| Classe | Precision | Recall | F1 | Support |
|---|---:|---:|---:|---:|
| Benign | 0.5352 | 0.9835 | 0.6932 | 5203 |
| DarkNexus | 0.7778 | 0.6196 | 0.6898 | 4961 |
| Generic | 0.0444 | 0.3017 | 0.0774 | 812 |
| Mirai | 0.8714 | 0.6037 | 0.7133 | 60857 |
| Other_rare | 0.0000 | 0.0000 | 0.0000 | 387 |
| Unknown | 0.1328 | 0.3053 | 0.1851 | 7881 |

## Diagnóstico da matriz de confusão
- 15 291 exemplos verdadeiramente Mirai foram classificados como Unknown.
- 3 847 exemplos Unknown foram classificados como Mirai.
- 366 de 387 exemplos Other_rare foram classificados como Mirai; 0 foram corretamente classificados.

**Limitação:** o modelo não reconhece Other_rare na validação. A avaliação ainda não demonstra desempenho adequado em todas as classes.

## Próximas tarefas
1. Verificar ausência de leakage, grupos e duplicados entre treino, validação e teste.
2. Confirmar que as classes raras estão presentes no treino e analisar a origem dos rótulos.
3. Fixar pipeline e hiperparâmetros sem usar os resultados de teste para os modificar.
4. Realizar avaliação final num conjunto de teste independente, se este existir e não tiver sido utilizado nas comparações.
5. Guardar métricas, matriz de confusão, versões de dependências e artefactos reproduzíveis.

Os valores aqui registados foram fornecidos pelos outputs do notebook em 27/10/2026; não foram recalculados nesta atualização.
