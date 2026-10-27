# Treino e avaliação de modelos

Foram experimentados Random Forest e Extra Trees para classificação multiclasse de tráfego IoT. Os resultados e limitações estão em [docs/avaliacao_random_forest.md](../../docs/avaliacao_random_forest.md).

O notebook de trabalho mais recente foi desenvolvido no Google Colab, incluindo uma pesquisa limitada de hiperparâmetros, validação completa e matriz de confusão. É necessário publicar/confirmar a versão final do notebook antes de declarar esta etapa reprodutível no repositório.

**Nota:** os dados de teste final não devem ser utilizados para escolher hiperparâmetros. Não guardar o dataset bruto nem grandes modelos `.joblib` no Git sem uma política adequada (por exemplo, Git LFS ou artefactos externos).
