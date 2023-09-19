import unittest
import sys
sys.path.append('..')
from arapiracanews import site_sete_segundos_news
import validators

class Test_setesegundos(unittest.TestCase):
    def test_noticias_vazia(self):
        noticias = site_sete_segundos_news()
        tam_noticias = len(noticias)
        tam_maior_que_zero = tam_noticias > 0
        self.assertTrue(tam_maior_que_zero,"Tamanho do dicionário é maior que zero")
    def test_validar_links(self):
        noticias = site_sete_segundos_news()
        for noticia in noticias:
            link_corrigido = "https://www.{}".format(noticia.get("link"))
            validacao = validators.url(link_corrigido)
            self.assertTrue(validacao,"Os links do dicionário de notícias são válidos")

if __name__ == '__main__':
    unittest.main()