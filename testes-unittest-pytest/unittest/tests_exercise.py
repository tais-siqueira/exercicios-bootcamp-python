def str_to_bool(value):  #A função str_to_bool() recebe uma cadeia de caracteres como entrada e seu trabalho é retornar True ou False dependendo do conteúdo da cadeia de caracteres.
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:   #se a cadeia de caracteres for y
        return True     # ela retornará True
    if value in false_values:   #se a cadeia de caracteres for no 
        return False     #ela retornará False
    
import unittest

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

#Como a função não vê 'Yes' como parte de nenhum dos valores, ela acaba retornando um None implícito, por isso o erro informa: None is not true.

def str_to_bool(value):
    try:
        value = value.lower()       #para que qualquer uma dessas opções deve funcionar: YES, YeS, yES, yes, yeS, Y, y.
    except AttributeError:        #se um valor com tipo diferente de cadeia de caracteres for usado:
        raise AttributeError(f"{value} must be of type string")    #Essa capitalização pode ser detectada capturando um AttributeError ao chamar value.lower() porque apenas as cadeias de caracteres têm um método lower():
    true_values = ['y','yes']
    false_values = ['no', 'n']

    if value in true_values:
        return True
    if value in false_values:
        return False
    
import unittest

class TestStrToBool(unittest.TestCase):

    def test_y_is_true(self):
        result = str_to_bool('y')
        self.assertTrue(result)

    def test_yes_is_true(self):
        result = str_to_bool('Yes')
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()

#Esse novo teste deve verificar se AttributeError é gerado pela entrada não cadeia de caracteres:
def test_invalid_input(self):
        with self.assertRaises(AttributeError):
            str_to_bool(1)
            
