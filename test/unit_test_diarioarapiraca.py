import unittest
import sys
sys.path.append('..')
from arapiracanews import diario_arapiraca_news
import validators

class Test_Diario_Arapiraca(unittest.TestCase):
    def test_noticias_vazia(self):
        noticias = diario_arapiraca_news()
        tam_noticias = len(noticias)
        tam_maior_que_zero = tam_noticias > 0
        self.assertTrue(tam_maior_que_zero,"Tamanho do dicionário de notícias é maior que zero")
    def test_validar_links(self):
        noticias = diario_arapiraca_news()
        for noticia in noticias:
            validacao = validators.url(noticia.get("link"))
            self.assertTrue(validacao,"Os links do dicionário de notícias são válidos")
        

if __name__ == '__main__':
    unittest.main()
    