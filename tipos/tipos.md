
# Aula Tipos

## Primitivos

Em python temos os seguintes tipos primitivos:

* int
* float / decimal
* string
* bool
* list / arrays

---

Para declarar uma variável utilizamos a seguinte sintaxe

*NOME_VARIAVEL* = **VALOR_VARIAVEL**

> Importante ressaltar que o sinal de igual aqui tem a função de atribuição, para comparação utilizamos de outra maneira que será visto mais a frente

```python
idade = 3 # int
peso = 78.5 # float
nome = 'João' # string
solteiro = true
caracteristicas = ['branco', 'alto', 'cabelos castanhos']
```

## Verificando os tipos

```python
print(type(idade))
print(type(peso))
print(type(nome))
print(type(solteiro))
print(type(caracteristicas))
```

## Complexos

```python
valores = (90, 79, 54, 32, 21) # Tuplas
altura = {'Amanda': 1.65, 'Ana': 1.60, 'João': 1.70} #Dicionário
print(type(valores))
print(type(altura))
```