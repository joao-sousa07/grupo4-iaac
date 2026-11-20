from pathlib import Path
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import (
    accuracy_score, precision_score, recall_score, f1_score,
    ConfusionMatrixDisplay, roc_curve, auc
)
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier

# 1. Resolução dinâmica do caminho do ficheiro e diretoria de figuras
SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = SCRIPT_DIR.parents[1]  # Raiz do repositório 'grupo4-iaac'
FILE_PATH = PROJECT_ROOT / 'data' / 'raw' / 'NSL_style_5class_dataset.csv'

# Criar a pasta reports/figures na raiz do projeto se não existir
FIGURES_DIR = PROJECT_ROOT / 'reports' / 'figures'
FIGURES_DIR.mkdir(parents=True, exist_ok=True)

print(f"A carregar o dataset a partir de:\n{FILE_PATH}\n")

if not FILE_PATH.exists():
    raise FileNotFoundError(f"Ficheiro não encontrado em: {FILE_PATH}")

df = pd.read_csv(FILE_PATH)

# Identificar a coluna target (última coluna do dataset)
target_col = df.columns[-1]

# 2. Mapeamento para Classificação Binária (0 = normal, 1 = comprometido)
df[target_col] = df[target_col].apply(lambda x: 0 if str(x).strip().lower() == 'normal' else 1)

# Separar atributos (X) e rótulos (y)
X = df.drop(columns=[target_col])
y = df[target_col]

# Codificação de variáveis categóricas (One-Hot Encoding)
X = pd.get_dummies(X, drop_first=True)

# 3. Divisão dos dados (80% Treino, 20% Teste)
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42, stratify=y
)

# Normalização dos atributos (necessária para a Regressão Logística)
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# 4. Configuração dos Modelos
models = {
    'Regressão Logística': LogisticRegression(max_iter=1000, random_state=42),
    'Random Forest': RandomForestClassifier(n_estimators=100, random_state=42, n_jobs=-1),
    'XGBoost': XGBClassifier(n_estimators=100, learning_rate=0.1, random_state=42, n_jobs=-1)
}

results = []
predictions = {}
probabilities = {}

# 5. Treino e Avaliação dos Modelos
for name, model in models.items():
    print(f"A treinar {name}...")
    
    if name == 'Regressão Logística':
        model.fit(X_train_scaled, y_train)
        y_pred = model.predict(X_test_scaled)
        y_prob = model.predict_proba(X_test_scaled)[:, 1]
    else:
        model.fit(X_train, y_train)
        y_pred = model.predict(X_test)
        y_prob = model.predict_proba(X_test)[:, 1]
    
    predictions[name] = y_pred
    probabilities[name] = y_prob
    
    acc = accuracy_score(y_test, y_pred)
    prec = precision_score(y_test, y_pred)
    rec = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)
    
    results.append({
        'Modelo': name,
        'Accuracy': f'{acc * 100:.2f}%',
        'Precision': f'{prec * 100:.2f}%',
        'Recall': f'{rec * 100:.2f}%',
        'F1-Score': f'{f1 * 100:.2f}%'
    })

# Apresentação dos Resultados em Tabela
results_df = pd.DataFrame(results)
print("\n" + "="*55)
print("       RESULTADOS DA AVALIAÇÃO DOS MODELOS")
print("="*55)
print(results_df.to_string(index=False))

# 6. Geração e Gravação dos Gráficos em 'reports/figures/'
class_names = ['Normal', 'Comprometido']

# 6.1 Guardar Matrizes de Confusão
fig, axes = plt.subplots(1, 3, figsize=(18, 5))
for ax, (name, y_pred) in zip(axes, predictions.items()):
    ConfusionMatrixDisplay.from_predictions(
        y_test, y_pred,
        display_labels=class_names,
        cmap=plt.cm.Blues,
        ax=ax,
        colorbar=False
    )
    ax.set_title(f'Matriz de Confusão - {name}')
plt.tight_layout()

cm_path = FIGURES_DIR / 'confusion_matrices.png'
plt.savefig(cm_path, dpi=300)
plt.close()
print(f"\n[Gráfico Guardado] Matrizes de Confusão: {cm_path}")

# 6.2 Guardar Curvas ROC Comparativas
plt.figure(figsize=(8, 6))
for name, y_prob in probabilities.items():
    fpr, tpr, _ = roc_curve(y_test, y_prob)
    roc_auc = auc(fpr, tpr)
    plt.plot(fpr, tpr, lw=2, label=f'{name} (AUC = {roc_auc:.4f})')

plt.plot([0, 1], [0, 1], color='navy', lw=2, linestyle='--')
plt.xlim([0.0, 1.0])
plt.ylim([0.0, 1.05])
plt.xlabel('Taxa de Falsos Positivos (FPR)')
plt.ylabel('Taxa de Verdadeiros Positivos (Recall)')
plt.title('Comparação de Curvas ROC')
plt.legend(loc="lower right")
plt.grid(True)

roc_path = FIGURES_DIR / 'roc_curves_comparison.png'
plt.savefig(roc_path, dpi=300)
plt.close()
print(f"[Gráfico Guardado] Curvas ROC: {roc_path}")