#Crie um programa que solicite uma senha e verifique se ela está correta
senha_correta = '12345'
senha_usuario = input("Digite a senha: ") #armazena String ou Numero

#Python leh um if dps o outro...

if senha_correta == senha_usuario:
    print("Senha correta!")
else:
    print("Senha Incorreta!")