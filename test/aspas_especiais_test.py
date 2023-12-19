import sys
sys.path.append('..')
import unittest
from arapiracanews import remover_aspas_especiais


class AspasEspeciaisTest(unittest.TestCase):
    def test_aspasespeciais(self):
        # Teste dois links defeituosos e um normal
        # As aspas especiais devem ser removidas
        link1_mock = """‘https://canaltech.com.br/saude/as-cinco-profissoes-
        que-aumentam-
        o-risco-de-demencia-na-velhice/’"""
        link2_mock = """https://www.omelete.com.br/series-tv/
        ‘one-piece’-jacob-betrand-visita"""
        link3_mock = """https://canaltech.com.br/apps/chrome-pode-ganhar-novos-
        controles-de-privacidade-em-breve-263699/"""
        link1_mock_fix = remover_aspas_especiais(link1_mock)
        self.assertEqual(link1_mock_fix.find("‘"), -1)
        self.assertEqual(link1_mock_fix.find("’"), -1)
        link2_mock_fix = remover_aspas_especiais(link2_mock)
        self.assertEqual(link2_mock_fix.find("‘"), -1)
        self.assertEqual(link2_mock_fix.find("’"), -1)
        link3_mock_fix = remover_aspas_especiais(link3_mock)
        self.assertEqual(link3_mock_fix.find("‘"), -1)
        self.assertEqual(link3_mock_fix.find("’"), -1)


if __name__ == '__main__':
    unittest.main()
