from collections import namedtuple
import shelve

menu = '''
=========================================================
Gerenciador de cadastro de Jogadores de League of Legends
=========================================================

1 - Adicionar Jogador
2 - Pesquisar Jogador
3 - Excluir Jogador
4 - Listar Jogador
5 - Sair

Digite uma opção: '''

eSport = shelve.open("eSport.db")
Jogador = namedtuple("Jogador", "nome nickname campeao funcao elo")
jogadores_tabela = "\n{:<3}{:<15}{:^10}{:^15}{:^15}{:^15}".format("ID", "NOME", "NICKNAME", "CAMPEÃO", "FUNÇÃO", "ELO")


def adicionarJogador():
	nome = input("\nDigite o nome do Jogador: ")
	if nome in eSport.keys():
		print("\nJogador já cadastrdo.")
		return

	nickname = input("Digite o nickname do Jogador: ")#Nome usado no jogo.
	campeao = input("Digite seus campeões mais jogados: ")#Personage que você usar no jogo.
	funcao = input("Digite sua funcao: ")#Qual a posição em que você joga.
	elo = input("Digite seu elo:")#Sua posição no rank de acordo com a sua habilidade no jogo.
	eSport[nome] = Jogador(nome, nickname, campeao, funcao, elo)
	print("\nJogador CADASTRADO COM SUCESSO!")


def pesquisarJogador():
	if not eSport:  # Se a lista nao tiver Jogador
		print("\nNÃO HÁ Jogador CADASTRADO.")

	else:
		Jogador_pesquisar = input("\nNome do Jogador: ")

		for ID, key in enumerate(eSport.keys()):
			if eSport[key].nome == Jogador_pesquisar:
				print(jogadores_tabela)
				imprimirJogador(ID, eSport[key])
				return

		print("\nJogador não encontrado.")


def excluirJogador():
	if listarJogadors():
		try:
			Jogador_excluir = int(input("\nID do Jogador para excluir: "))
			if Jogador_excluir <= 0 or Jogador_excluir > len(eSport):
				print("\nID não existe!")
		except:
			print("\nEntrada inválida!")
			return

		for ID, key in enumerate(eSport.keys()):
			if ID == Jogador_excluir - 1:
				del eSport[key]
				print("\nJogador excluido sucesso.")


def listarJogadors():
	if not eSport:  # Se a lista nao tiver Jogador
		print("\nNão há Jogador cadastrdo.")
		return False

	else:
		print("{:=^70}".format("  TODOS OS JOGADORES CADASTRADOS  "))
		print(jogadores_tabela)
		for ID, key in enumerate(eSport.keys()):
			imprimirJogador(ID, eSport[key])

		return True

def imprimirJogador(ID, jogador):
        print("{:<3}{:<15}{:^10}{:^15}{:^15}{:^15}".format(ID + 1,
	jogador.nome,
	jogador.nickname,
	jogador.campeao,
	jogador.funcao,
        jogador.elo,))


while True:
	try:
		op = int(input(menu))
	except:
		print("\nENTRADA INVÁLIDA!")
		continue

	if op == 5:
		eSport.close()
		break
	elif op == 1:
		adicionarJogador()
	elif op == 2:
		pesquisarJogador()
	elif op == 3:
		excluirJogador()
	elif op == 4:
		listarJogadors()
	else:
		print("\nOPÇÃO INVALIDA!")


exit()
