from sklearn.metrics import (
    accuracy_score,
    classification_report,
    confusion_matrix,
    f1_score,
    precision_score,
    recall_score,
)

# y_true: valores reais do dataset
# y_pred: valores previstos pelo modelo
y_true = [0, 1, 1, 0, 1, 0, 0, 1, 1, 0]
y_pred = [0, 1, 0, 0, 1, 0, 1, 1, 1, 0]

# 1. Cálculo de todas as métricas principais
exatidao = accuracy_score(y_true, y_pred)
precisao = precision_score(y_true, y_pred)  # Foca-se em reduzir falsos positivos[cite: 17]
recall = recall_score(
    y_true, y_pred
)  # Foca-se em reduzir falsos negativos[cite: 17]
f1 = f1_score(
    y_true, y_pred
)  # Média harmónica, ideal para datasets desequilibrados[cite: 18]

# 2. Matriz de Confusão e Cálculo da Especificidade
cm = confusion_matrix(y_true, y_pred)
tn, fp, fn, tp = cm.ravel()  # Extrai Verdadeiros/Falsos Negativos e Positivos
especificidade = tn / (tn + fp) if (tn + fp) > 0 else 0

# 3. Apresentação organizada dos resultados
print('========================================')
print('   RELATÓRIO COMPLETO DE AVALIAÇÃO')
print('========================================')
print(f'Exatidão (Accuracy)    : {exatidao:.2f}')
print(f'Precisão (Precision)   : {precisao:.2f}')
print(f'Recall (Sensibilidade) : {recall:.2f}')
print(f'Especificidade         : {especificidade:.2f}')
print(f'F1 Score               : {f1:.2f}[cite: 18]\n')

print('--- Relatório Detalhado por Classe ---')
print(classification_report(y_true, y_pred))

print('--- Matriz de Confusão (TN, FP, FN, TP) ---')
print(cm)
print(f'Verdadeiros Negativos (TN): {tn}')
print(f'Falsos Positivos (FP)     : {fp}')
print(f'Falsos Negativos (FN)     : {fn}')
print(f'Verdadeiros Positivos (TP): {tp}')