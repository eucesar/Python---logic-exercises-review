# pegar o range = do numero 2 ao 11, vai pulando de 2 em 2 até 11 = '2,11' dps quando vai pular = '2' => set pq pertence a outra propriedade FOR
pares = set(range(2, 11, 2)) #par - n conta o 11 chega ate 10
impares = set(range(11, 21, 2)) #impar

# Unir os dois conjuntos usando o operador | (ou o método union) = suma
uniao = pares | impares

# Imprimir o conjunto resultante
print(uniao)