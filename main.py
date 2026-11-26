
import palpite
import ranking
import os
import random
lista_palpites = []
n = 1


corridas = [
    "AUS",
    "CHN",
    "JPN",
    "MIA",
    "CAN",
    "MON",
    "BAR",
    "AUT",
    "GBR",
    "BEL",
    "HUN",
    "NED",
    "ITA",
    "ESP",
    "AZE",
    "BAH",
    "SGP",
    "USA",
]

nomes_corridas = {
    "AUS": "GP da Austrália",
    "CHN": "GP da China",
    "JPN": "GP do Japão",
    "MIA": "GP de Miami",
    "CAN": "GP do Canadá",
    "MON": "GP de Mônaco",
    "BAR": "GP de Barcelona",
    "AUT": "GP da Áustria",
    "GBR": "GP da Grã-Bretanha",
    "BEL": "GP da Bélgica",
    "HUN": "GP da Hungria",
    "NED": "GP dos Países Baixos",
    "ITA": "GP da Itália",
    "ESP": "GP da Espanha",
    "AZE": "GP do Azerbaijão",
    "BAH": "GP do Bahrein",
    "SGP": "GP de Singapura",
    "USA": "GP dos Estados Unidos",
}
corrida_atual = random.choice(corridas)
nome_corrida = nomes_corridas[corrida_atual]
def limpar_terminal():
  os.system("cls" if os.name == "nt" else "clear")

print("Bem-vindo ao programa de palpites da Fórmula 1!\n")
#Loop do menu inicial
while True:
  print("1 - Registrar palpite")
  print("2 - Ver ranking")
  print("3 - Sair")
  opcao = input("Escolha uma opção: ")
  if opcao == "1":
    limpar_terminal()
    print(corrida_atual)
    palpite.registra_palpite(n, lista_palpites, corrida_atual, nome_corrida)  
  elif opcao == "2":
    limpar_terminal()
    ranking.ver_ranking(corrida_atual, nome_corrida)
  elif opcao == "3":
    print("Saindo do programa...")
    exit()
  else:
    print("Opção inválida, tente novamente.\n")


