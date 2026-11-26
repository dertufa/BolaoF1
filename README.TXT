Grupo:
Diogo: Programação (main.py/ palpite.py)
Paulo: Programação (palpite.py/ ranking.py)
Túlio: Programação (palpite.py, revisão e modularização do código)

Projeto: Pneu macio

Descrição: 
	Sistema em Python para registrar palpites do Top 10 em corridas de Fórmula 1, calcular a pontuação de cada jogador com base nos resultados oficiais e manter o ranking da rodada e o ranking geral atualizados.

	Funcionalidades: 

		Registro e validação de palpites: Exibição da corrida em foco e da lista de pilotos, com  salvamento automático do palpite em arquivo .txt.

		Cálculo de pontuação: cruzamento dos palpites com os dados do arquivo .csv, somando pontos por posição exata (10 a 1) e bônus de 1 ponto por acerto de piloto no Top 10 fora da posição exata.

		Persistência de dados: armazenamento de palpites e consolidação contínua da pontuação acumulada dos participantes em arquivos de texto.   

		Estrutura de Arquivos:
		main.py — Menu principal, controle de fluxo e seleção da corrida da rodada.   
		palpite.py — Exibição dos pilotos, validação das escolhas e gravação dos palpites.   
		ranking.py — Leitura do CSV, cálculo de pontuação e atualização dos rankings.  
		lista_palpites.txt — Base de palpites registrados pelos jogadores.   
		resultsf1.csv — Planilha com os resultados das corridas por etapa.   
		ranking.txt — Histórico acumulado do ranking geral.   