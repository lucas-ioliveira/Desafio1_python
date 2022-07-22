'''
* Criar variáveis para nome, idade
* Altura e peso de uma pessoa
* Criar variável com o ano atual
* Obter o ano de nascimento da pessoa
* Obter o IMC da pessoa com 2 casas decimais
* Exibir um texto com todos os valores na tela usando F-String
'''

nome = 'Lucas'
idade = 25
altura = 1.75
peso = 80
data_atual = 2022
imc = (peso / altura ** 2)
nasceu = (data_atual - idade)



print(f'{nome} tem {idade} anos, {altura} de altura e pesa {peso} Kg.')
print(f'O IMC de Lucas é: {imc:.2f}.')
print(f'{nome} nasceu em {nasceu}.')

