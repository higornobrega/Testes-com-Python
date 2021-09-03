from unittest import TestCase
from .dominio import Avaliador, Lance, Leilao, Usuario

class TestAvaliador(TestCase):

    def teste_retorna_maior_menor_valor_adicionado_crescente(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_do_yuri = Lance(yuri, 100)
        lance_do_gui = Lance(gui, 150)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_yuri)
        leilao.lances.append(lance_do_gui)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def teste_retorna_maior_menor_valor_adicionado_descrecente(self):
        gui = Usuario('Gui')
        yuri = Usuario('Yuri')

        lance_do_yuri = Lance(yuri, 100)
        lance_do_gui = Lance(gui, 150)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_gui)
        leilao.lances.append(lance_do_yuri)

        avaliador = Avaliador()
        avaliador.avalia(leilao)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, avaliador.menor_lance)
        self.assertEqual(maior_valor_esperado, avaliador.maior_lance)
    
    def teste_retorna_maior_menor_valor_apenas_um_lance(self):
        gui = Usuario('Gui')
        
        lance_do_gui = Lance(gui, 150)

        leilao = Leilao('Celular')

        leilao.lances.append(lance_do_gui)
        
        avaliador = Avaliador()
        avaliador.avalia(leilao)

        self.assertEqual(150, avaliador.maior_lance)
        self.assertEqual(150, avaliador.menor_lance)
