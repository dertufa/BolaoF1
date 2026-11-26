import ast
import csv
import random


def up_ranking(lista_rk):
  with open("ranking.txt", "w", encoding="utf-8") as rk:
    for item in lista_rk:
      rk.write(f"{item},\n")

#Mostra o Ranking de usuarios
def ver_ranking(abc,nome_corrida):
  lista_pp = []#lista de pontuação da rodada
  lista_rk = []#lista com o ranking geral
  results = []# results' e 'top10' se referem aos dados da planilha
  top10 = []
  points = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

  
  
  #Abre o .csv com os resultados das corridas
  with open("resultsf1.csv", "r", newline="", encoding="utf-8") as f1:
    reader = csv.DictReader(f1)
    for row in reader:
      pos = {"posição": row[abc], "carro": int(row["Nº"])}
      if pos["posição"].isdigit():
        pos["posição"] = int(pos["posição"])
        if pos["posição"] <= 10:
          results.append(pos)

  results.sort(key=lambda x: x["posição"])
  top10 = [item["carro"] for item in results]

  print(f"Corrida: {nome_corrida} ({abc}) - Resultado:")
  print("1º 2º 3º 4º 5º 6º 7º 8º 9º 10º")
  print(top10)

  with open("lista_palpites.txt", "r", encoding="utf-8") as lp:
    for linha in lp:
      linha = linha.strip()
      if linha:
        pp = ast.literal_eval(linha)
        if isinstance(pp, tuple):
          pp = pp[0]
        lista_pp.append(pp)

  for jogador_pp in lista_pp:
    pontos = 0
    cars = jogador_pp["palpite"]
    for j in range(len(top10)):
      if j < len(cars) and cars[j] == top10[j]:
        pontos += points[j]
      elif j < len(cars) and cars[j] in top10:
        pontos += 1
    jogador_pp["pontuação"] = pontos

  lista_pp.sort(key=lambda item: item["pontuação"], reverse=True)
  print("\nRanking da rodada:\n")
  for idx, jogador_pp in enumerate(lista_pp, start=1):
    print(f"{idx}º {jogador_pp['nome']} - {jogador_pp['pontuação']} pts")

  try:
    with open("ranking.txt", "r", encoding="utf-8") as rank:
      for linhas in rank:
        dado = linhas.strip().rstrip(",")
        if dado:
          rnk = ast.literal_eval(dado)
          if isinstance(rnk, tuple):
            rnk = rnk[0]
          lista_rk.append(rnk)
  except FileNotFoundError:
    lista_rk = []

  for jogador_pp in lista_pp:
    encontrou = False
    for jogador_rk in lista_rk:
      if jogador_pp["nome"] == jogador_rk["nome"]:
        jogador_rk["pontuação"] += jogador_pp["pontuação"]
        encontrou = True
        break
    if not encontrou:
      lista_rk.append({
          "nome": jogador_pp["nome"],
          "pontuação": jogador_pp["pontuação"],
      })

  lista_rk.sort(key=lambda item: item["pontuação"], reverse=True)
  print("\nRanking Geral:\n")
  for idx, jogador_rk in enumerate(lista_rk, start=1):
    print(f"{idx}º {jogador_rk['nome']} - {jogador_rk['pontuação']} pts")

  up_ranking(lista_rk)