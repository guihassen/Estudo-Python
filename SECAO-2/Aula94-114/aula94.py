# Funções decoradoras e decoradores
# Decorar = Adicionar / Remover/ Restringir / Alterar
# Funções decoradoras são funções que decoram outras funções
# Decoradores são usados para fazer o Python
# usar as funções decoradoras em outras funções.


def create_function(func):
    def interna(*args,**kwargs):
        for arg in args :
            is_string(arg)
        resultado = func(*args,**kwargs)
        print(f"O seu resultado foi {resultado}")
        return resultado
    return interna


def inverte_string (string) :
    return string[::-1]

def is_string (param):
    if not isinstance(param,str):
        raise TypeError("Deve ser uma string")

string_check = create_function(inverte_string)
invertida = inverte_string("4321")
print(invertida)
    