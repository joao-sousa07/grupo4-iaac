
import sys
import unittest
from pathlib import Path
from unittest.mock import patch, Mock

import requests

BASE = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(BASE / "ia_generativa"))

from explicar_ameaca import explicar_ameaca


class TestesIAGenerativa(unittest.TestCase):

    @patch("explicar_ameaca.requests.post")
    def test_malware_mirai(self, mock_post):
        resposta = Mock()
        resposta.json.return_value = {
            "response": "Mirai é uma família de malware IoT."
        }
        mock_post.return_value = resposta

        resultado = explicar_ameaca("Mirai")

        self.assertIn("Mirai", resultado)

        pedido = mock_post.call_args.kwargs["json"]
        self.assertEqual(pedido["model"], "llama3.2")
        self.assertIn("Mirai", pedido["prompt"])

    @patch("explicar_ameaca.requests.post")
    def test_trafego_benigno(self, mock_post):
        resposta = Mock()
        resposta.json.return_value = {
            "response": "Tráfego benigno não garante segurança."
        }
        mock_post.return_value = resposta

        resultado = explicar_ameaca("Benign")

        self.assertIn("benigno", resultado.lower())

        pedido = mock_post.call_args.kwargs["json"]
        self.assertIn("BENIGNO", pedido["prompt"])

    @patch("explicar_ameaca.requests.post")
    def test_ollama_desligado(self, mock_post):
        mock_post.side_effect = requests.exceptions.ConnectionError()

        resultado = explicar_ameaca("Mirai")

        self.assertIn("Erro", resultado)
        self.assertIn("Ollama", resultado)

    @patch("explicar_ameaca.requests.post")
    def test_timeout(self, mock_post):
        mock_post.side_effect = requests.exceptions.Timeout()

        resultado = explicar_ameaca("Mirai")

        self.assertIn("Erro", resultado)

    @patch("explicar_ameaca.requests.post")
    def test_resposta_vazia(self, mock_post):
        resposta = Mock()
        resposta.json.return_value = {"response": ""}
        mock_post.return_value = resposta

        resultado = explicar_ameaca("Mirai")

        self.assertIn("Erro", resultado)


if __name__ == "__main__":
    unittest.main(verbosity=2)
