import os
import joblib
import pandas as pd
import numpy as np
import ollama

from sklearn.model_selection import GridSearchCV, StratifiedKFold
from sklearn.ensemble import RandomForestClassifier
from sklearn.svm import SVC
from xgboost import XGBClassifier
from sklearn.metrics import (
    confusion_matrix, 
    recall_score, 
    precision_score, 
    f1_score, 
    roc_auc_score
)

class OllamaPhishingAgent:
    """
    Agente de IA responsável por orquestrar o treino dos modelos de ML,
    guardar o modelo vencedor na pasta 'models/' e gerar relatórios executivos
    com o Ollama (LLM Local).
    """
    def __init__(self, ollama_model="llama3.2", random_state=42):
        self.ollama_model = ollama_model
        self.random_state = random_state
        self.best_model = None
        self.best_model_name = ""
        self.trained_models = {}

    def train_and_optimize(self, X_tr, y_tr):
        print("\n🤖 [Agente IA] A treinar e otimizar modelos (Random Forest, XGBoost, SVM)...")
        cv = StratifiedKFold(n_splits=5, shuffle=True, random_state=self.random_state)

        # 1. Random Forest otimizado
        param_grid = {'n_estimators': [100, 150], 'max_depth': [10, 20, None]}
        grid_rf = GridSearchCV(
            RandomForestClassifier(random_state=self.random_state),
            param_grid=param_grid, cv=cv, scoring='recall', n_jobs=-1
        )
        grid_rf.fit(X_tr, y_tr)
        self.trained_models['Random Forest'] = grid_rf.best_estimator_

        # 2. XGBoost
        xgb = XGBClassifier(random_state=self.random_state, eval_metric='logloss')
        xgb.fit(X_tr, y_tr)
        self.trained_models['XGBoost'] = xgb

        # 3. SVM
        svm = SVC(probability=True, random_state=self.random_state)
        svm.fit(X_tr, y_tr)
        self.trained_models['SVM'] = svm

        print("🤖 [Agente IA] Treino de modelos concluído!")

    def evaluate(self, X_te, y_te):
        best_recall = -1.0
        results = []

        for name, model in self.trained_models.items():
            preds = model.predict(X_te)
            probs = model.predict_proba(X_te)[:, 1]

            rec = recall_score(y_te, preds)
            prec = precision_score(y_te, preds)
            f1 = f1_score(y_te, preds)
            auc = roc_auc_score(y_te, probs)

            results.append({
                'Modelo': name, 
                'Precision': round(prec, 4),
                'Recall': round(rec, 4), 
                'F1-Score': round(f1, 4), 
                'ROC-AUC': round(auc, 4)
            })

            if rec > best_recall:
                best_recall = rec
                self.best_model = model
                self.best_model_name = name

        return pd.DataFrame(results)

    def save_best_model(self, scaler, models_dir="models"):
        """Guarda o modelo vencedor e o scaler na pasta 'models/'."""
        os.makedirs(models_dir, exist_ok=True)
        
        model_path = os.path.join(models_dir, "phishing_best_model.pkl")
        scaler_path = os.path.join(models_dir, "phishing_scaler.pkl")
        
        joblib.dump(self.best_model, model_path)
        joblib.dump(scaler, scaler_path)
        
        print(f"💾 [Modelo Guardado] O modelo '{self.best_model_name}' foi guardado em: {model_path}")
        print(f"💾 [Scaler Guardado] O Normalizador foi guardado em: {scaler_path}")

    def generate_llm_report(self, y_te, X_te):
        """Gera o parecer executivo recorrendo ao Ollama."""
        print(f"\n🦙 [Ollama Agent] A comunicar com o modelo local '{self.ollama_model}'...")
        preds = self.best_model.predict(X_te)
        cm = confusion_matrix(y_te, preds)
        tn, fp, fn, tp = cm.ravel()

        prompt = f"""
        És um Especialista Sénior em Cibersegurança e Inteligência Artificial.
        Analisa os seguintes resultados do modelo de Deteção de Phishing URLs para um relatório do ISTEC:

        - Modelo Vencedor: {self.best_model_name}
        - Verdadeiros Positivos (Phishing detetado): {tp}
        - Falsos Negativos (Phishing NÃO detetado - Risco Crítico): {fn}
        - Falsos Positivos (Legítimo bloqueado): {fp}
        - Verdadeiros Negativos (Legítimo correto): {tn}
        - Recall (Sensibilidade): {recall_score(y_te, preds)*100:.2f}%
        - Precision: {precision_score(y_te, preds)*100:.2f}%
        - F1-Score: {f1_score(y_te, preds)*100:.2f}%

        Escreve um Parecer Técnico Executivo curto (3 parágrafos) em Português de Portugal para o relatório:
        1. Avalia o desempenho do modelo e a importância de registar apenas {fn} Falsos Negativos.
        2. Explica a vantagem técnica do {self.best_model_name} na deteção de ameaças.
        3. Dá uma recomendação prática de implementação numa infraestrutura de rede.
        """

        try:
            response = ollama.chat(model=self.ollama_model, messages=[{'role': 'user', 'content': prompt}])
            print("\n======================================================================")
            print("🦙 PARECER TÉCNICO GERADO PELO OLLAMA")
            print("======================================================================")
            print(response['message']['content'])
            print("======================================================================\n")
        except Exception as e:
            print(f"⚠️ Aviso no Ollama: {e}")