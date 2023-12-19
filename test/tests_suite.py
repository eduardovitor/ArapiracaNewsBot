import unittest

from aspas_especiais_test import AspasEspeciaisTest
from formatacao_test import FormatacaoTest
from validacao_test import ValidacaoTest


def suite():
    suite = unittest.TestSuite()
    suite.addTest(AspasEspeciaisTest("test_aspasespeciais"))
    suite.addTest(FormatacaoTest("test_formatar"))
    suite.addTest(ValidacaoTest("test_validar"))
    return suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite())