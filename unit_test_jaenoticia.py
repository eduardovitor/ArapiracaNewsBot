import unittest
from arapiracanews import jaenoticiaNews
import validators

class Test_Jaenoticia(unittest.TestCase):
    def test_noticias_vazia(self):
        noticias = jaenoticiaNews()
        tam_noticias = len(noticias)
        tam_maior_que_zero = tam_noticias > 0
        self.assertTrue(tam_maior_que_zero,"Tamanho do dicionário é maior que zero")
    def test_validar_links(self):
        noticias = jaenoticiaNews()
        for noticia in noticias:
            validacao = validators.url(noticia.get("link"))
            self.assertTrue(validacao,"Os links do dicionário de notícias são válidos")

if __name__ == '__main__':
    unittest.main()