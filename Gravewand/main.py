from time import sleep
print('_' * 35)
print('Gravewand'.center(30))
print('_' * 35 )
while True:
	name=str(input('Como você gostaria de ser chamado? ' )).strip() .capitalize()
	print(f'Seja bem vindo {name}')
	if name == "S":
		print('Vamos começar nossa aventura!')
		print('''=========ESCOLHA SUA CLASSE==========
		[ A ] Mago 
		[ B ] Guerreiro
		[ C ] Ladrão
		[ D ] Paladino
		[ E ] Necromance''')
	classe = str(input("Faça uma boa escolha! ")).strip().upper()
	if classe == "A":
			print('Você escolheu mago U!')
			print('Boa para ser jogada de longo alcance')			
	if classe == "B":
			print('Você escolheu guerreiro!')
			print('Lento mais tem uma resistência absurda')
	elif classe == "C":
			print('Você escolheu ladrão!')
			print('Classe lenta mas com uma agilidade ótima')
	elif classe == "D":
			print('Você escolheu Paladino!')
			print('Uma excelente resistência e uma ótima força')
	elif classe == "E":
			print('Você escolheu Necromance!')
			print('Classe boa para um combate de perto e de longe')
while True:
	print('''====={name}=====
	[ 1 ] Inventário
	[ 2 ] Loja
	[ 3 ] Quests
	[ 4 ] Monatarias
	[ 5 ] Ver seu ouro''')
	e= int(input("O que você deseja?"))
	if e == 1:
		print('Por enquanto você só tem uma espada de madeira')
		r=str(input('Deseja equipar [S/N] ')).strip().upper()[0]
		if r == "S":
			print('Voce equipou sua espada de madeira!')
		elif r == "N":
			print("Saindo do inventário...")
			break
if e == 2:
	print('No momento você não tem ouro o suficiente')
if e == 3:
	print( "Você tem uma quests  para fazer")
if e == 4:
	print('Você ainda nao tem nenhuma montaria') 
elif e == 5:
	print('Você no momento ainda nao tem nenhum ouro')

 					