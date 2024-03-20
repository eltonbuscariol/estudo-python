
feminino:bool = True
idade:int = 17 # int
peso:float = 74.5 #float
nome:str = 'Felipe' #string
estado_civil:str = 'Solteiro' # bool
cadastro = {
    "nome": 'Felipe',
    'idade': 17,
    'peso': 74.5,
    'solteiro': True,
    'sexo': 'Masculino',
    'caracteristicas': {
        'cor': 'branco',
        'cabelo': 'preto',
        'olhos': 'castanhos'
    }
}
'''
Condicionais

Se feminino for igual a verdadeiro então imprima Correto
senão imprime Incorreto

'''

if feminino:
    print('Correto')
else:
    print('Incorreto')

'''
Se a idade for maior ou igual 16 então imprime 'Idade correta'
senão imprime 'Idade inferior ao permitido'
'''
limite_idade = 18
if idade >= limite_idade:
    print('Idade correta')
else:
    print('Idade inferior ao permitido')

'''
Se estado civil for igual a solteiro então imprime 'Correto'
senão se for igual a casado imprime 'Incorreto'
senão se for igual a divorciado imprime 'Correto'
senão imprime 'Correto'
'''

if estado_civil == 'Solteiro':
    print('Correto')
elif estado_civil == 'Casado':
    print('Incorreto')
elif estado_civil == 'Divorciado':
    print('Correto')
else:
    print('Correto')

'''
Operadores:

== 'igual'
!= 'Diferente'
> 'Maior'
< 'Menor'
>= 'Maior ou igual'
<= 'Menor ou igual'
'''

# Se o nome felipe está no dicionário
if 'olhos' in cadastro['caracteristicas'] and cadastro['caracteristicas']['olhos'] == 'castanhos':
    print('Correto')
else:
    print('Incorreto')