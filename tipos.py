# Tipos primitivos

'''
int = numero inteiro = 1
float = flutuando = numero radical = 1.33
string = texto = 'Texto'
bool = boleano = true / false
list = lista / array = [1,2,3,4]
'''

idade:int = 17 # int
peso:float = 74.5 #float
nome:str = 'Felipe' #string
solteiro:bool = True # bool
caracteristicas:list = ['branco', 'cabelo preto', 'olhos castanhos'] # list

'''
Tipos complexos

tuple = tupla = ('Felipe', 17, 74.5, True, ['branco', 'cabelo preto', 'olhos castanhos'])
dict = dicionário = {}
'''

retorno = ('Felipe', 17, 74.5, True, ['branco', 'cabelo preto', 'olhos castanhos'])
cadastro = {
    "nome": 'Felipe',
    'idade': 17,
    'peso': 74.5,
    'solteiro': True,
    'caracteristicas': {
        'cor': 'branco',
        'cabelo': 'preto',
        'olhos': 'castanhos'
    }
}

print(cadastro['caracteristicas']['cabelo'])

