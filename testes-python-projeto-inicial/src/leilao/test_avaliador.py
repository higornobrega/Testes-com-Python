from unittest import TestCase
from .dominio import Avaliador, Lance, Leilao, Usuario

class TestAvaliador(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui')
        self.lance_do_gui = Lance(self.gui, 150)
        self.leilao = Leilao('Celular')


    def teste_retorna_maior_menor_valor_adicionado_crescente(self):
        yuri = Usuario('Yuri')

        lance_do_yuri = Lance(yuri, 100)
       

        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def teste_retorna_maior_menor_valor_adicionado_descrecente(self):
        yuri = Usuario('Yuri')

        lance_do_yuri = Lance(yuri, 100.0)

        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(self.lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def teste_retorna_maior_menor_valor_apenas_um_lance(self):
        self.leilao.lances.append(self.lance_do_gui)
        
        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        self.assertEqual(150, avaliador.maior_lance)
        self.assertEqual(150, avaliador.menor_lance)

    def teste_retorna_maior_menor_valor_adicionado_com_tres_lances(self):
        yuri = Usuario('Yuri')
        fer = Usuario('Fer')

        lance_do_yuri = Lance(yuri, 100)
        lance_do_fer = Lance(fer, 200)

        self.leilao.lances.append(lance_do_yuri)
        self.leilao.lances.append(lance_do_fer)

        avaliador = Avaliador()
        avaliador.avalia(self.leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    