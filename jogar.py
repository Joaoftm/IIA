# -*- coding: utf-8 -*-
## Plataforma Alfa-Beta
## Definição:
## - do  tipo ResultadoJogo
## - de funções para realizar jogos.
##

from collections import namedtuple
import random
import jogos_iia

"""
O resultado de um jogo é um tuplo com três componentes:
- O tipo de resultado. Tipicamente: 'vitoria' ou 'empate', mas
poderão existir variantes, dependendo do jogo.
- A cor associada ao resultado. Tipicamente: 'brancas' ou 'pretas'. Poderá 
também ser outro valor, por exemplo,'nenhum', nos casos em que há empate.
- O nome do jogador vencedor, ou 'nenhum', no caso de empate.
"""

ResultadoJogo = namedtuple('ResultadoJogo','tipo, cor, nome')

# ______________________________________________________________________________
# Players for Games


def query_player(game, state, nivel = 0):
    """Make a move by querying standard input."""
#    print("current state:")
#    game.display(state)
    print("available moves: {}".format(game.actions(state)))
    print("")
    move_string = input('Your move? ')
    try:
        move = eval(move_string)
    except NameError:
        move = move_string
    return move


def random_player(game, state, nivel = 0):
    """A player that chooses a legal move at random."""
    return random.choice(game.actions(state))


def alphabeta_player(game, state, nivel = 0):
    return jogos_iia.alphabeta_search(state, game)


class Jogador:
    """Um jogador tem três atributos:
    - jogo - o jogo a que está associado 
    - nome - uma representação em string do seu nome
    - funcao - a função que o concretiza
    """
    
    def __init__(self, jogo, nome = "Anónimo", f = None) :
        self.jogo = jogo
        self.nome = nome
        if f == None :
            self.funcao = query_player
        else :
            self.funcao = f



                           
def um_jogo(game, jogador1, jogador2, nivel, verbose = False) :
    """
    """
    estado = game.initial
    if verbose :
        game.display(estado)
    
    fim = False
    jogs = [jogador1,jogador2]
    ind_proximo = 0
    
    while not fim :
        jogada = jogs[ind_proximo].funcao(game,estado,nivel)
        estado = game.result(estado,jogada)
        if verbose :
            game.display(estado)
        fim = game.terminal_test(estado)
        ind_proximo = 1 - ind_proximo
    
    utilidade = game.utility(estado, game.to_move(game.initial))
    if utilidade == 1 :
        resultado = ResultadoJogo('vitoria',game.jogadores[0],jogador1.nome)
    elif utilidade == -1 :
        resultado = ResultadoJogo('vitoria',game.jogadores[1],jogador2.nome)
    else :
        resultado = ResultadoJogo('empate','nenhum','nenhum')
    
    return resultado


def um_par_de_jogos(game,j1,j2,nivel,verbose = False) :
    """
    Realização de um par de jogos entre dois jogadores, de modo a que cada
    jogador faça um jogo em cada lado ('brancas' ou pretas')
    É devolvido um par de resultados.
    """
    r1 = um_jogo(game,j1,j2,nivel,verbose)
    r2 = um_jogo(game,j2,j1,nivel,verbose)
    return (r1,r2)

def n_pares_de_jogos(game,n,j1,j2,nivel,verbose = False) :
    """Realização de n pares de jogos entre os jogadores j1 e j2, 
    alternando os papéis (brancas ou pretas) de cada jogador.
    É devolvido um 5-tuplo com:
    - número de vitórias de j1 jogando com as brancas
    - número de vitórias de j1 jogando com as pretas
    - número de vitórias de j2 jogando com as brancas
    - número de vitórias de j1 jogando com as pretas
    - númeor de empates
    """
    vit1B, vit1P, vit2B, vit2P, emp = (0,0,0,0,0)
    for _ in range(n) :
        (r1,r2) = um_par_de_jogos(game,j1,j2,nivel,verbose)
        if r1.tipo == "empate" :
            emp += 1
        elif r1.cor == game.jogadores[0] :
            vit1B += 1
        else :
            vit2P += 1
        if r2.tipo == "empate" :
            emp += 1
        elif r2.cor == game.jogadores[0] :
            vit2B += 1
        else :
            vit1P += 1
    
    return vit1B, vit1P, vit2B, vit2P, emp
    
    