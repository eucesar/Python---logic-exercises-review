#Instale e use um pacote externo, como o pandas ou o numpy

# Instalando o pacote pandas usando o comando pip
!pip install pandas

# Importando o pacote pandas
import pandas as pd

# Criando um DataFrame a partir de um dicionário => armazena array, : .
dados = {'Nome': ['Alice', 'Bob', 'Carlos', 'Daniel'],
         'Idade': [25, 30, 35, 40],
         'Cidade': ['São Paulo', 'Rio de Janeiro', 'Belo Horizonte', 'Porto Alegre']}
DataFrame = pd.DataFrame(dados) #armazena os dados

# Imprimindo o DataFrame - impra oque foi armazenado
print(DataFrame)

