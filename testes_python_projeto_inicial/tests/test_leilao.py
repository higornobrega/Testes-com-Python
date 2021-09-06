from src.leilao.excecoes import LanceInvalido
from unittest import TestCase

from src.leilao.dominio import Leilao, Usuario, Lance



class TestLeilao(TestCase):

    def setUp(self):
        self.gui = Usuario('Gui', 500)
        self.lance_do_gui = Lance(self.gui, 150)
        self.leilao = Leilao('Celular')


    def teste_retorna_maior_menor_valor_adicionado_crescente(self):
        yuri = Usuario('Yuri', 500)

        lance_do_yuri = Lance(yuri, 100)
       

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(self.lance_do_gui)

        
        menor_valor_esperado = 100.0
        maior_valor_esperado = 150.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def teste_nao_deve_permitir_propor_um_lance_em_ordem_descrecente(self):
        with self.assertRaises(LanceInvalido):
            yuri = Usuario('Yuri', 500)

            lance_do_yuri = Lance(yuri, 100.0)
            self.leilao.propoe(self.lance_do_gui)

            self.leilao.propoe(lance_do_yuri)
    
    def teste_retorna_maior_menor_valor_apenas_um_lance(self):
        self.leilao.propoe(self.lance_do_gui)
        
       
        self.assertEqual(150, self.leilao.maior_lance)
        self.assertEqual(150, self.leilao.menor_lance)

    def teste_retorna_maior_menor_valor_adicionado_com_tres_lances(self):
        yuri = Usuario('Yuri', 500)
        fer = Usuario('Fer', 500)

        lance_do_yuri = Lance(yuri, 100)
        lance_do_fer = Lance(fer, 200)

        self.leilao.propoe(lance_do_yuri)
        self.leilao.propoe(lance_do_fer)

        menor_valor_esperado = 100.0
        maior_valor_esperado = 200.0

        self.assertEqual(menor_valor_esperado, self.leilao.menor_lance)
        self.assertEqual(maior_valor_esperado, self.leilao.maior_lance)
    
    def test_deve_permitir_lance_caso_nao_tenha_lance(self):
        self.leilao.propoe(self.lance_do_gui)
        quantidade_de_lances_recebidos = len(self.leilao.lances)
        
        self.assertEqual(1, quantidade_de_lances_recebidos)

    def test_deve_permitir_propor_um_lance_caso_o_ultimo_usuario_seja_diferente(self):
        yuri = Usuario('Yuri', 500)
        lance_do_yuri = Lance(yuri,200.0)
        
        self.leilao.propoe(self.lance_do_gui)
        self.leilao.propoe(lance_do_yuri)
        quantidade_de_lances_recebidos = len(self.leilao.lances)

        self.assertEqual(2, quantidade_de_lances_recebidos)

    def test_nao_deve_permitir_propor_lance_caso_o_usuario_for_o_mesmo(self):
        Lance_do_gui200 = Lance(self.gui, 200)
        with self.assertRaises(LanceInvalido):
            self.leilao.propoe(self.lance_do_gui)
            self.leilao.propoe(Lance_do_gui200)
