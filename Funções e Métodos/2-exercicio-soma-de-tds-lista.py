#Crie uma função que recebe uma lista como parâmetro e retorna a soma de todos os elementos
def somar_elementos(lista): #função soma
    
    total = 0 # valor total da lista, vai somar elemento por elemento com o valor 0 => 0 + 1 dps 0 + 2 dps....
    for elemento in lista: #elemento = item da lista - 1 lugar pra prencher é o elemento da lista
        total += elemento
    return total #valor atualizado

#pode ser o msm nome da função
lista = [1, 2, 3, 4, 5]
resultado = somar_elementos(lista)
print(resultado)