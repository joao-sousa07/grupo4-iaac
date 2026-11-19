
import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO_IA = "llama3.2"


def explicar_ameaca(familia):
    familia = str(familia).strip()

    if familia.lower() == "benign":
        prompt = """
        És um assistente de cibersegurança.

        Um modelo Random Forest classificou uma
        amostra de tráfego IoT como BENIGNO.

        Explica em português de Portugal:
        1. O que significa esta classificação.
        2. Porque não garante segurança absoluta.
        3. Que boas práticas devemos manter.

        Não afirmes que o dispositivo está seguro.
        Responde de forma clara e objetiva.
        """
    else:
        prompt = f"""
        És um assistente de cibersegurança.

        Um Random Forest classificou uma amostra
        de tráfego IoT como possível malware
        da família {familia}.

        Explica em português de Portugal:
        1. O que se sabe sobre esta família.
        2. Quais são os possíveis riscos.
        3. Que medidas de proteção são recomendadas.

        Não afirmes que a infeção foi confirmada.
        Não inventes indicadores técnicos.
        Se não conheceres a família, indica-o.
        """

    try:
        resposta = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO_IA,
                "prompt": prompt,
                "stream": False,
                "options": {"temperature": 0.2}
            },
            timeout=180
        )

        resposta.raise_for_status()
        texto = resposta.json().get("response", "").strip()

        if not texto:
            raise ValueError("O Llama devolveu uma resposta vazia.")

        return texto

    except requests.exceptions.ConnectionError:
        return (
            "Erro: não foi possível comunicar com o Ollama. "
            "Confirma se o Ollama está em execução."
        )

    except requests.exceptions.Timeout:
        return "Erro: o Llama demorou demasiado a responder."

    except (requests.exceptions.RequestException, ValueError) as erro:
        return f"Erro ao gerar a explicação: {erro}"


if __name__ == "__main__":
    print(explicar_ameaca("Mirai"))
