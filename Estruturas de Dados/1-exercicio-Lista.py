#Crie uma lista de números e ordene-os de forma crescente e decrescente

numero = [4,6,2,1,8,9,6,3]

#sorted padrão separa os numeros em ordens crescentes
numeroCrescente = sorted(numero)
print("Array de numero crescente: ", numeroCrescente)

#reverse do sorted, coloco 1° qual variavel quero manipular dps virgula a função reverse e verdadeira (como se usasse ponto) - delicado com letras maiuscula ou menuscula
numeroDecrescente = sorted(numero, reverse=True)
print("Array de nuemro decrescente: ", numeroDecrescente)
