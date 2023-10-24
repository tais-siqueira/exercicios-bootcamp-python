def str_to_bool(string):    #A função str_to_bool() aceita uma cadeia de caracteres como entrada e, dependendo de seu conteúdo, retornará um valor de verdadeiro ou falso.
    if string.lower() in ['yes', 'y', '1']:
        return True
    elif string.lower() in ['no', 'n', '0']:
        return False
    
#anexe os testes para a função str_to_bool(). Use pytest.mark.parametrize() para testar todos os valores verdadeiros primeiro:
import pytest 

@pytest.mark.parametrize("string", ['Y', 'y', '1', 'YES'])
def test_str_to_bool_true(string):
    assert str_to_bool(string) is True
    
#Em seguida, acrescente outro teste com os valores falsos:
@pytest.mark.parametrize("string", ['N', 'n', '0', 'NO'])
def test_str_to_bool_false(string):
    assert str_to_bool(string) is False
    
#Embora você tenha escrito apenas duas funções de teste, Pytest foi capaz de criar oito testes no total graças à função parametrize().

#Esse teste deve usar uma função setup() e teardown() que cria um arquivo temporário com algum texto. Após cada teste, o arquivo é removido.
import os


class TestFile:

    def setup(self):
        with open("/tmp/done", 'w') as _f:
            _f.write("1")

    def teardown(self):
        try:
            os.remove("/tmp/done")
        except OSError:
            pass

    def test_done_file(self):
        with open("/tmp/done") as _f:
            contents = _f.read()
        assert contents == "1"
        
#A classe de teste está garantindo que um arquivo seja criado, mas isso é problemático porque ela está usando o caminho /tmp/,que não tem a garantia de estar presente em todos os sistemas.

import pytest

@pytest.fixture
def tmpfile(tmpdir):
    def write():
        file = tmpdir.join("done")
        file.write("1")
        return file.strpath
    return write

#O acessório tmpfile() usa o acessório tmpdir() de Pytest, que garante um arquivo temporário válido que é limpo após a conclusão dos testes.

class TestFile:

    def test_f(self, tmpfile):
     path = tmpfile()
     with open(path) as _f:
        contents = _f.read()
     assert contents == "1"
    
#Essa classe de teste agora pode garantir que um arquivo temporário seja criado e limpo com o conteúdo adequado para que a declaração funcione.