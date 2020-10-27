#!/usr/bin/env python3
# -*- coding: utf-8 -*-

## Plataforma Alfa-Beta

## Implementação do jogo Hobbes

import jogos_iia
from copy import deepcopy

LINHAS = 5
COLUNAS = 5
MAX_JOGADAS = 50
    
class JogoHobbes(jogos_iia.Game) :
  """Representação para o jogo:
  """
  
  @staticmethod
  def outro_jogador(jogador) :
    return 'b' if jogador == 'p' else 'p'
      
  @staticmethod
  def get_posicao_atual(tabuleiro, jogador) :
    posicao = tuple()
    for p, j in tabuleiro.items() :
      if j == jogador :
        posicao = p
        break
    return posicao

  @staticmethod
  def get_acessiveis(tabuleiro, a_visitar) :
    acessiveis = a_visitar[:]
    while a_visitar != [] :
      x, y = a_visitar[0]
      direita  = (x + 1, y)
      esquerda = (x - 1, y)
      baixo    = (x, y - 1)
      cima     = (x, y + 1)
      if x < COLUNAS and direita not in tabuleiro \
                     and direita not in acessiveis :
        a_visitar.append(direita)
        acessiveis.append(direita)
      if x > 1 and esquerda not in tabuleiro \
               and esquerda not in acessiveis:
        a_visitar.append(esquerda)
        acessiveis.append(esquerda)
      if y > 1 and baixo not in tabuleiro \
               and baixo not in acessiveis :
        a_visitar.append(baixo)
        acessiveis.append(baixo)
      if y < LINHAS and cima not in tabuleiro \
                    and cima not in acessiveis :
        a_visitar.append(cima)
        acessiveis.append(cima)
      a_visitar = a_visitar[1:]
    return acessiveis

  @staticmethod
  def find_movs(tabuleiro, acessiveis, casa) :
    movs = list()
    x, y = casa
    direita  = (x + 1, y)
    esquerda = (x - 1, y)
    baixo    = (x, y - 1)
    cima     = (x, y + 1)
    if direita in tabuleiro and tabuleiro[direita] == 'n' :
      if x < COLUNAS - 1:
        for i in range(x + 2, COLUNAS + 1) :
          if (i, y) not in tabuleiro or (i, y) in acessiveis:
            movs += [(casa, (i - 1, y))]
          else :
            break
      if x > 2:
        for i in range(x - 1, 0, -1) :
          if (i, y) in acessiveis:
            movs += [(casa, (i, y))]
          else :
            break
    if esquerda in tabuleiro and tabuleiro[esquerda] == 'n' :
      if x > 2:
        for i in range(x - 2, 0, -1) :
          if (i, y) not in tabuleiro or (i, y) in acessiveis:
            movs += [(casa, (i + 1, y))]
          else :
            break
      if x < COLUNAS :
        for i in range(x + 1, COLUNAS + 1) :
          if (i, y) in acessiveis :
            movs += [(casa, (i, y))]
          else :
            break
    if baixo in tabuleiro and tabuleiro[baixo] == 'n' :
      if y > 2:
        for i in range(y - 2, 0, -1) :
          if (x, i) not in tabuleiro or (x, i) in acessiveis:
            movs += [(casa, (x, i + 1))]
          else :
            break
      if y < LINHAS:
        for i in range(y + 1, LINHAS + 1) :
          if (x, i) not in tabuleiro or (x, i) in acessiveis:
            movs += [(casa, (x, i))]
          else :
            break
    if cima in tabuleiro and tabuleiro[cima] == 'n' :
      if y < LINHAS - 1:
        for i in range(y + 2, LINHAS + 1) :
          if (x, i) not in tabuleiro or (x, i) in acessiveis:
            movs += [(casa, (x, i - 1))]
          else :
            break
      if y > 1 :
        for i in range(y - 1, 0, -1) :
          if (x, i) in acessiveis :
            movs += [(casa, (x, i))]
          else :
            break
    return movs

  @staticmethod
  def movimentos_possiveis(tabuleiro, jogador) :
    posicao_atual = JogoHobbes.get_posicao_atual(tabuleiro, jogador)
    movs = list()
    a_visitar = [posicao_atual]
    acessiveis = JogoHobbes.get_acessiveis(tabuleiro, a_visitar)
    a_visitar = acessiveis[:]
    while a_visitar != [] :
      movs += JogoHobbes.find_movs(tabuleiro, acessiveis, a_visitar[0])
      a_visitar = a_visitar[1:]
    return movs

  def __init__(self) :
    self.jogadores = ('p', 'b')
    tabuleiro_inicial = {(2, 1): 'n', (2, 2): 'n', (2, 4): 'n', (2, 5): 'n',
                         (3, 1): 'p', (3, 2): 'n', (3, 4): 'n', (3, 5): 'b',
                         (4, 1): 'n', (4, 2): 'n', (4, 4): 'n', (4, 5): 'n'}
    movs_possiveis = self.movimentos_possiveis(tabuleiro_inicial,
                                               self.jogadores[0])
    self.initial = jogos_iia.GameState(to_move = self.jogadores[0],
                                       utility = 0,
                                       board = (0, tabuleiro_inicial),
                                       moves = movs_possiveis)

  def actions(self, state) :
    return state.moves

  def result(self, state, move) :
    """
    Requires: 'move' é uma jogada válida no estado dado ('state')
    """
    tabuleiro = deepcopy(state.board[1])
    jogador_atual = state.to_move
    proximo_jogador = self.outro_jogador(jogador_atual)
    num_jogadas = state.board[0]
    #print("move: {}".format(move))
    posicao_1 = self.get_posicao_atual(state.board[1], jogador_atual)
    posicao_2, posicao_3 = move
    x_1, y_1 = posicao_2
    x_2, y_2 = posicao_3
    if x_1 < x_2 :
      if (x_1 + 1, y_1) in tabuleiro and tabuleiro[(x_1 + 1, y_1)] == 'n' :
        del tabuleiro[(x_1 + 1, y_1)]
        tabuleiro[(x_2 + 1, y_1)] = 'n'
      else :
        del tabuleiro[(x_1 - 1, y_1)]
        tabuleiro[(x_2 - 1, y_1)] = 'n'
    elif x_1 > x_2 :
      if (x_1 - 1, y_1) in tabuleiro and tabuleiro[(x_1 - 1, y_1)] == 'n' :
        del tabuleiro[(x_1 - 1, y_1)]
        tabuleiro[(x_2 - 1, y_1)] = 'n'
      else :
        del tabuleiro[(x_1 + 1, y_1)]
        tabuleiro[(x_2 + 1, y_1)] = 'n'
    elif y_1 < y_2 :
      if (x_1, y_1 + 1) in tabuleiro and tabuleiro[(x_1, y_1 + 1)] == 'n' :
        del tabuleiro[(x_1, y_1 + 1)]
        tabuleiro[(x_1, y_2 + 1)] = 'n'
      else :
        del tabuleiro[(x_1, y_1 - 1)]
        tabuleiro[(x_1, y_2 - 1)] = 'n'
    else :
      if (x_1, y_1 - 1) in tabuleiro and tabuleiro[(x_1, y_1 - 1)] == 'n' :
        del tabuleiro[(x_1, y_1 - 1)]
        tabuleiro[(x_1, y_2 - 1)] = 'n'
      else :
        del tabuleiro[(x_1, y_1 + 1)]
        tabuleiro[(x_1, y_2 + 1)] = 'n'
    if posicao_1 in tabuleiro and tabuleiro[posicao_1] == jogador_atual :
        del tabuleiro[posicao_1]
    tabuleiro[(x_2, y_2)] = jogador_atual
    novo_board = (num_jogadas + 1, tabuleiro)
    movimentos = self.movimentos_possiveis(tabuleiro, proximo_jogador)
    utilidade = self.calcular_utilidade(tabuleiro, 
                                        jogador_atual, 
                                        proximo_jogador, 
                                        movimentos)
    estado = jogos_iia.GameState(to_move = proximo_jogador,
                                 board = novo_board,
                                 moves = movimentos,
                                 utility = utilidade)
    return estado

  def calcular_utilidade(self, tabuleiro, jogador, prox_jogador, movimentos) :
    utilidade = 0
    pos_atual = self.get_posicao_atual(tabuleiro, jogador)
    x_1, y_1 = pos_atual
    adversario = self.outro_jogador(jogador)
    pos_adversario = self.get_posicao_atual(tabuleiro, adversario)
    x_2, y_2 = pos_adversario
    if (x_1 == x_2 + 1 and y_1 == y_2) or (x_1 == x_2 - 1 and y_1 == y_2) \
                                       or (y_1 == y_2 + 1 and x_1 == x_2) \
                                       or (y_1 == y_2 - 1 and x_1 == x_2) :
      if jogador == prox_jogador :
        utilidade = 1
      else :
        utilidade = -1
    elif movimentos == [] :
      if jogador == prox_jogador :
        utilidade = -1
      else :
        utilidade = 1  
    return utilidade

  def utility(self, state, player):
    return self.calcular_utilidade(state.board[1], 
                                   player, state.to_move, state.moves)

  def terminal_test(self, state) :
    return state.board[0] == MAX_JOGADAS \
             or any([self.utility(state, x) != 0 for x in self.jogadores])

  def display(self, state):
    tabuleiro = state.board[1]
    print("Tabuleiro actual:")
    for y in range(1, LINHAS + 1):
      for x in range(1, COLUNAS + 1):
        if (x, y) in tabuleiro :
          print(tabuleiro[(x, y)], end=' ')
        else :
          print('.',end=' ')
      print()
    if self.terminal_test(state) :
      print("FIM do Jogo")
    else :
      print("\nPróximo jogador: {}\n".format(state.to_move))