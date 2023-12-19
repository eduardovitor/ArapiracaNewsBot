import unittest
import sys
sys.path.append('..')
import json
from arapiracanews import validar_dados


class ValidacaoTest(unittest.TestCase):
    def test_validar(self):
        contar_validas = 0
        with open('noticias.json') as json_file:
            noticias_mock = json.load(json_file)
        for e in noticias_mock:
            if validar_dados(e["link"], e["titulo"]):
                contar_validas += 1
        self.assertEqual(contar_validas, 6, "Há 6 links válidos")


if __name__ == '__main__':
    unittest.main()