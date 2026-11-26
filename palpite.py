

pilotos = [
    "12 - Antonelli | 63 - Russell",
    "16 - Leclerc | 44 - Hamilton",
    "3 - Verstappen | 6 - Hadjar",
    "1 - Norris | 81 - Piastri",
    "30 - Lawson | 41 - Lindblad",
    "10 - Gasly | 43 - Colapinto",
    "5 - Bortoleto | 27 - Hulkenberg",
    "31 - Ocon | 87 - Bearman",
    "23 - Albon | 55 - Sainz",
    "14 - Alonso | 18 - Stroll",
    "11 - Perez | 77 - Bottas",
]
carros = [
    12,
    63,
    16,
    44,
    3,
    6,
    1,
    81,
    30,
    41,
    10,
    43,
    5,
    27,
    31,
    87,
    23,
    55,
    14,
    18,
    11,
    77,
]

lista_palpites = []
n = 1


#Escreve os palpites coletados no arquivo de texto
def add_palpite(dados_pp):
  with open("lista_palpites.txt", "a", encoding="utf-8") as dp:
    dp.write(f"{dados_pp}\n")

#registra os palpites
def registra_palpite(n,lista_palpites, sigla_corrida, nome_corrida):
    print(f"Corrida atual: {nome_corrida} ({sigla_corrida})\n")
    nome_jogador = input("Digite o nome do jogador: ").strip()
    print( "\nFaça seu palpite usando os números dos pilotos.\nDigite 0 (zero) para cancelar.\n")
    for p in range(len(pilotos)):
        print(pilotos[p])
        

    # Laço while para palpites, com mensagem de erro para numero errado/repetido e opção de cancelar
    while n < 11:
        palpites = int(input(f"Digite o {n}º colocado: "))
        if palpites == 0:
            print("Palpite cancelado!")
            break
        elif palpites in carros:
            if palpites in lista_palpites:
                print("Número repetido, tente novamente.")
                continue
            else:
                lista_palpites.append(palpites)
                n += 1
        else:
            print("Número inválido, tente novamente.")
            continue

    #Prepara os dados coletados pra ir pra lista e chama a função que faz isso         
    if n > 10:
        novo_jogador = {"nome": nome_jogador, "palpite": lista_palpites}  
        add_palpite(novo_jogador)  
        print(f"\nPalpite de {nome_jogador} registrado com sucesso!")



