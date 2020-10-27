#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Jogadores alfabeta para o jogo Hobbes (com funções de avaliação)

import jogos_iia
import hobbes_jogo_35
from math import sqrt

def f_aval_hobbes_F1(estado, jogador):
  if estado.utility == 1 :
    valor = 1000
  elif estado.utility == -1 :
    valor = -1000
  else :
    enemy = hobbes_jogo_35.JogoHobbes.outro_jogador(jogador)
    player_moves = estado.moves if estado.to_move == jogador else \
                 hobbes_jogo_35.JogoHobbes.movimentos_possiveis(
                         estado.board[1], jogador)
    enemy_moves = estado.moves if estado.to_move == enemy else \
                 hobbes_jogo_35.JogoHobbes.movimentos_possiveis(
                         estado.board[1], enemy)
    f = len(player_moves) - len(enemy_moves)
  return f

def f_aval_hobbes_35_1(estado, jogador) :
  if estado.utility == 1 :
    valor = 1000
  elif estado.utility == -1 :
    valor = -1000
  else :
    tabuleiro = estado.board[1]
    posicao = hobbes_jogo_35.JogoHobbes.get_posicao_atual(tabuleiro, jogador)
    x_1, y_1 = posicao
    aprox_centro_Jogador = -sqrt((3 - x_1)**2 + (3 - y_1)**2)
    valor = aprox_centro_Jogador
  return valor
  
def f_aval_hobbes_35_2(estado, jogador) :
  if estado.utility == 1 :
    valor = 1000
  elif estado.utility == -1 :
    valor = -1000
  else :
    tabuleiro = estado.board[1]
    posicao = hobbes_jogo_35.JogoHobbes.get_posicao_atual(tabuleiro, jogador)
    x_1, y_1 = posicao
    dist_centro_jogador = sqrt((3 - x_1)**2 + (3 - y_1)**2)
    outro = hobbes_jogo_35.JogoHobbes.outro_jogador(jogador)
    posicao_outro = hobbes_jogo_35.JogoHobbes.get_posicao_atual(
            tabuleiro, outro)
    x_2, y_2 = posicao_outro
    dist_centro_outro = sqrt((3 - x_2)**2 + (3 - y_2)**2)
    valor = dist_centro_outro - dist_centro_jogador
  return valor

def jogador_hobbes_35_1(jogo, estado, nivel = 3) :
  return jogos_iia.alphabeta_cutoff_search(
            estado, jogo, nivel, eval_fn = f_aval_hobbes_35_1)
    
def jogador_hobbes_35_2(jogo, estado, nivel = 3) :
  return jogos_iia.alphabeta_cutoff_search(
            estado, jogo, nivel, eval_fn = f_aval_hobbes_35_2)

def jogador_hobbes_F1(jogo, estado, nivel = 3) :
  return jogos_iia.alphabeta_cutoff_search(
            estado, jogo,nivel, eval_fn = f_aval_hobbes_F1)
