import json
import unittest
import sys
sys.path.append('..')
from arapiracanews import formatar_msg


class FormatacaoTest(unittest.TestCase):
    def test_formatar(self):
        site_mock = "Já é notícia News\n\n"
        with open('noticias.json') as json_file:
            noticias_mock = json.load(json_file)
        msg = formatar_msg(noticias_mock, site_mock)
        self.assertIsNotNone(msg, "Retorno da formatação não deve ser nulo")
        self.assertIsInstance(msg, str, "Mensagem deve ser uma string")
        self.assertTrue(len(msg) > 0, "A mensagem deve ter vários caracteres")


if __name__ == '__main__':
    unittest.main()
