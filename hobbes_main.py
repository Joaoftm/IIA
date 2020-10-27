#!/usr/bin/env python3
# -*- coding: utf-8 -*-
## Main - Jogo Hobbes

#Módulos genéricos
import jogar     # utlidades para realizar jogos

# Módulos específicos do jogo Hobbes
import hobbes_jogo_35
import hobbes_jogadores_35

jogo = hobbes_jogo_35.JogoHobbes()

j1 = jogar.Jogador(jogo, "Hobbes1", hobbes_jogadores_35.jogador_hobbes_35_1)
j2 = jogar.Jogador(jogo, "Hobbes2", hobbes_jogadores_35.jogador_hobbes_35_2)
j3 = jogar.Jogador(jogo, "F1",hobbes_jogadores_35.jogador_hobbes_F1)
j4 = jogar.Jogador(jogo,"Ao Calhas",f = jogar.random_player)

resultado1 = jogar.um_jogo(jogo, j2, j3, 3, True)
print('\n{}'.format(resultado1))

#njogos = jogar.n_pares_de_jogos(jogo,10,j2,j3,3)
#print(njogos)
