import sys
import os

# Garantir acesso à pasta src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'src')))

from data_processing import load_and_preprocess_data
from ai_agent import OllamaPhishingAgent

def main():
    print("🚀 === INICIANDO PIPELINE AUTÓNOMO DE DETEÇÃO DE PHISHING ===")
    
    # 1. Carregamento e Pré-processamento
    X_train, X_test, y_train, y_test, scaler, feature_names = load_and_preprocess_data()
    
    # 2. Inicialização do Agente IA
    agent = OllamaPhishingAgent(ollama_model="llama3.2")
    
    # 3. Treino e Otimização dos Modelos
    agent.train_and_optimize(X_train, y_train)
    
    # 4. Avaliação e Comparação
    df_results = agent.evaluate(X_test, y_test)
    
    print("\n=== TABELA RESUMO DE RESULTADOS ===")
    print(df_results.to_string(index=False))
    
    # 5. Guardar Modelo e Scaler na pasta models/
    models_dir = os.path.abspath(os.path.join(os.path.dirname(__file__), 'models'))
    agent.save_best_model(scaler, models_dir=models_dir)
    
    # 6. Gerar Relatório Executivo com Ollama
    agent.generate_llm_report(y_test, X_test)
    
    print("\n✅ === PIPELINE CONCLUÍDO COM SUCESSO ===")

if __name__ == "__main__":
    main()