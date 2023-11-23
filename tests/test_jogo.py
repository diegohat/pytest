# def test_meu_primeiro_teste():
#     assert True
from pytest import mark, fixture
from source.jogo import brincadeira
import sys

def test_quando_brincadeira_receber_1_entao_deve_retornar_1():
    # entrada = 1 # given
    # esperado = 1 # given
    # resultado = brincadeira(1) # when
    # assert resultado == esperado # then

    # Versão One-step test
    assert brincadeira(1) == 1

def test_quando_brincadeira_receber_2_entao_deve_retornar_2():
    assert brincadeira(2) == 2

def test_quando_brincadeira_receber_3_entao_deve_retornar_queijo():
    assert brincadeira(3) == "queijo"

@mark.goiabada
def test_quando_brincadeira_receber_5_entao_deve_retornar_goiabada():
    assert brincadeira(5) == "goiabada"

@mark.goiabada
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == "goiabada"

@mark.skip(reason="ainda não implementei")
def test_quando_brincadeira_receber_10_entao_deve_retornar_goiabada():
    assert brincadeira(10) == "goiabada"

@mark.parametrizado
@mark.parametrize(
    "entrada",
    [5, 10, 20, 25, 35]
)
def test_brincadeira_deve_retornar_goiabada_com_multiplos_de_5(entrada):
    assert brincadeira(entrada) == "goiabada"

@mark.parametrizado2
@mark.parametrize(
    "entrada, esperado",
    [(1, 1), (2, 2), (3, "queijo"), (4, 4),(5, "goiabada")]
)
def test_brincadeira_deve_retornar_valor_esperado(entrada, esperado):
    assert brincadeira(entrada) == esperado

@mark.windows
@mark.skipif(
    sys.platform == "linux",
    reason="Não funciona no Linux"
)
def test_skip_windows():
    assert brincadeira(20) != "goiabada"

@mark.stdout
def test_brincadeira_deve_escrever_entrei_na_brincadeira_na_tela(capsys):
    brincadeira(0)
    resultado = capsys.readouterr()
    assert resultado.out == "Entrei na brincadeira\n"

@fixture
def minha_fixture():
    """Essa fixture é um teste."""
    return -1

@mark.exemplo_fixture
def test_minha_fixture_em_acao(minha_fixture):
    print(minha_fixture)