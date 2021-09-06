from src.leilao.dominio import Leilao, Usuario

def test_deve_subtrair_o_valor_da_carteira_quando_este_propor_um_lance():
    vini = Usuario('Vine', 100)
    leilao = Leilao('Celular')
    vini.propor_lance(leilao, 50.0)

    assert vini.carteira == 50.0