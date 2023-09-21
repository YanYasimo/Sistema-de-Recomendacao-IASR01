import pytest

@pytest.mark.slow
def test_calculo_demorado():
    # Simula um cálculo demorado
    resultado = 0
    for i in range(100000000):
        resultado += i
    assert resultado == 4999999950000000

@pytest.mark.fast
def test_calculo_rapido():
    # Simula um cálculo rápido
    resultado = 0
    for i in range(10):
        resultado += i
    assert resultado == 45

@pytest.mark.slow
def test_calculo_demorado2():
    # Simula um cálculo demorado
    resultado = 0
    for i in range(5000000):
        resultado += i
    assert resultado == 100000000