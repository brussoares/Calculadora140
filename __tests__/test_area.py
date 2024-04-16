import pytest

from area.area import calcular_area_de_um_quadrado, calcular_area_de_um_retangulo, calcular_area_de_um_triangulo
from utils.utils import ler_csv


# 2 - Crie os testes de unidade para essas três funções que criou na questão 1
def test_calcular_area_de_um_quadrado():
    lado = 2
    resultado_esperado = 4
    resultado_obtido = calcular_area_de_um_quadrado(lado)

    assert resultado_esperado == resultado_obtido

def test_calcular_area_de_um_retangulo():
    comprimento = 2
    largura = 5
    resultado_esperado = 10
    resultado_obtido = calcular_area_de_um_retangulo(comprimento, largura)

    assert resultado_esperado == resultado_obtido

def test_calcular_area_de_um_triangulo():
    base = 5
    altura = 10
    resultado_esperado = 25
    resultado_obtido = calcular_area_de_um_triangulo(base, altura)

    assert resultado_esperado == resultado_obtido

# 3 - Altere um desses testes de unidade para que leia uma massa de teste a partir de uma lista de valores
@pytest.mark.parametrize('comprimento, largura, resultado_esperado',
                         [ (2, 10, 20),
                           (5, 10, 50),
                           (10, 10, 100),
                           (4, 2, 8)
                         ]
                         )
def test_calcular_area_de_um_retangulo_lista(comprimento, largura, resultado_esperado):

    resultado_obtido = calcular_area_de_um_retangulo(comprimento, largura)

    assert resultado_esperado == resultado_obtido


# 4 - Altere outro desses testes de unidade para que leia uma massa de teste a partir de um arquivo csv
@pytest.mark.parametrize('base, altura, resultado_esperado',
                            ler_csv('./fixtures/massa_area_triangulo.csv')
                         )
def test_calcular_area_de_um_trinagulo_csv(base, altura, resultado_esperado):

    resultado_obtido = calcular_area_de_um_triangulo(float(base), float(altura))

    assert float(resultado_esperado) == resultado_obtido