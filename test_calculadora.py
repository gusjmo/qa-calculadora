import pytest
from calculadora import somar, subtrair, multiplicar, dividir

# ===== TESTES DE SOMA =====
def test_somar_positivos():
    assert somar(2, 3) == 5

def test_somar_negativos():
    assert somar(-1, -1) == -2

def test_somar_zero():
    assert somar(0, 5) == 5

# ===== TESTES DE SUBTRAÇÃO =====
def test_subtrair_positivos():
    assert subtrair(10, 4) == 6

def test_subtrair_resultado_negativo():
    assert subtrair(3, 10) == -7

# ===== TESTES DE MULTIPLICAÇÃO =====
def test_multiplicar_positivos():
    assert multiplicar(3, 4) == 12

def test_multiplicar_por_zero():
    assert multiplicar(5, 0) == 0

# ===== TESTES DE DIVISÃO =====
def test_dividir_positivos():
    assert dividir(10, 2) == 5

def test_dividir_resultado_decimal():
    assert dividir(7, 2) == 3.5

def test_dividir_por_zero():
    with pytest.raises(ValueError):
        dividir(10, 0)
