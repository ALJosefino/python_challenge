import os
#greetings
print("Olá usuária(o) este é um cadastro de nome, telefone e endreço")

#customer name
#input
print(" por favor digite seu nome: ")
name = input()
#output
print(" seja bem vinda(o) " + name)

#customer phone
#input
print(" agora, digite o número do seu telefone: ")
phone = input()
#output
print(name + " o número digitado por você foi: " + phone)

#customer address
#input
print(" por último, digite seu endereço: ")
address = input()
#output
print(name + " o endereço digitado por você foi: " + address)

os.system('clear')

#every outputs together
print(name + " obrigado por digitar seu telefone que é: " + phone + " e seu endereço: " + address)

#farewells
print("Até logo!")