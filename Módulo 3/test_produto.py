from produto import Produto
import pytest

@pytest.fixture
def produto():
    return Produto(1, 'Teste', 1.0, 10)

def test_constructor(produto):
    assert produto.id == 1
    assert produto.nome == 'Teste'
    assert produto.preco == 1.0
    assert produto.estoque == 10

def test_aumentarEstoque(produto):
    produto.aumentarEstoque(10)
    assert produto.estoque == 20

def test_diminuirEstoque(produto):
    produto.diminuirEstoque(5)
    assert produto.estoque == 5