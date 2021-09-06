from _pytest.fixtures import fixture
from src.leilao.dominio import Leilao, Usuario
import pytest

@pytest.fixture
def vini():
    return Usuario('Vine', 100)

@pytest.fixture
def leilao():
    return Leilao('Celular')


def test_deve_subtrair_o_valor_da_carteira_quando_este_propor_um_lance(vini, leilao):
    vini.propor_lance(leilao, 50.0)

    assert vini.carteira == 50.0

def test_lance_maior_que_o_valor_da_carteira(vini, leilao):
    with pytest.raises(ValueError):
        vini.propor_lance(leilao, 150.0)

   

def test_deve_permitir_o_lance_quando_o_valor_for_menor_que_a_carteira(vini, leilao):
    vini.propor_lance(leilao, 50.0)

    assert vini.carteira == 50.0


def test_lance_igual_que_o_valor_da_carteira(vini, leilao):
    vini.propor_lance(leilao, 100.0)
    
    assert vini.carteira == 0
    

