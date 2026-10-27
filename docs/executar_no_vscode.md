# Executar os notebooks IAAC no VS Code (Windows)

## 1. Instalar o Python

Utilizar **Python 3.12 de 64 bits**. Confirmar versões instaladas no PowerShell:

```powershell
py -0p
```

Caso não esteja instalado, instalar a versão 3.12 x64 através do site oficial do Python. Evitar o Python 3.14 de 32 bits que anteriormente causou dificuldades de instalação.

## 2. Clonar o projeto e entrar na branch individual

No terminal do VS Code:

```powershell
git clone https://github.com/joao-sousa07/grupo4-iaac.git
cd grupo4-iaac
git fetch origin
git switch joao-sousa
```

Se a pasta já existir, abrir essa pasta e executar `git fetch origin` e `git switch joao-sousa` — não clonar por cima da pasta existente.

## 3. Criar um ambiente Python local

```powershell
py -3.12 -m venv .venv
.\.venv\Scripts\python.exe -m pip install --upgrade pip
.\.venv\Scripts\python.exe -m pip install -r requirements-local.txt
.\.venv\Scripts\python.exe -m ipykernel install --user --name grupo4-iaac --display-name "Python (grupo4-iaac)"
```

Estes comandos funcionam sem ativar o ambiente no PowerShell.

## 4. Executar o notebook

1. Instalar as extensões **Python** e **Jupyter** da Microsoft no VS Code.
2. Abrir `notebooks/1_data_preparation/data_preparation_otimizado_v4_avaliacao_final.ipynb`.
3. No canto superior direito, selecionar **Select Kernel** → **Python (grupo4-iaac)**.
4. Executar as células por ordem. A primeira célula `%pip install ...` pode ser dispensada quando as dependências já foram instaladas pelo ficheiro `requirements-local.txt`.

O notebook chama `kagglehub.dataset_download(...)` e procura o CSV na cache local do KaggleHub. É necessária ligação à Internet no primeiro download. **Não copiar o dataset completo para dentro do repositório.**

## 5. RAM e desempenho

- Fechar aplicações pesadas antes de treinar.
- Começar pelas configurações de baixo consumo de memória.
- Não aumentar o número de árvores nem o paralelismo até confirmar a utilização de RAM.
- As primeiras execuções podem demorar; os resultados anteriores não são automaticamente reproduzidos num novo ambiente.
- Se aparecer `MemoryError`, reduzir `MAX_TRAIN_TUNING` de 100000 para 50000 e `n_jobs` para 1 e repetir a experiência de forma documentada. Isso pode alterar as métricas e exige nova validação.
- Para evitar repetir treinos, guardar os artefactos `.joblib` localmente ou numa localização apropriada. Não os adicionar ao Git normal.

## 6. Guardar progresso no GitHub

```powershell
git status
git add docs/ notebooks/
git commit -m "docs: atualizar resultados da avaliação local"
git push origin joao-sousa
```

Rever os ficheiros incluídos antes do commit; não publicar datasets, credenciais ou modelos pesados. 

## 7. Avaliação final

O notebook v4 inclui auditoria e avaliação no conjunto de teste. Executar o teste final **somente depois** de fixar o candidato e confirmar que este conjunto não foi usado para otimização. Os resultados finais serão guardados em `resultados_avaliacao_final/` e podem ser transcritos para `docs/avaliacao_random_forest.md`.
