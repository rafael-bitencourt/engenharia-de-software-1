import math
from rodada import Rodada

class Jogo:
    def __init__(self, player_interface, jogadores):
        print("-> JOGO INICIADO")
        self.__player_interface = player_interface
        self.__jogadores = jogadores
        self.__numero_da_rodada = 1
        self.determinar_primeiro_jogador()
        self.__rodada = Rodada(self.__player_interface, self.__jogadores, self.__numero_da_rodada)
        self.__terminou = False

    def determinar_primeiro_jogador(self):
        for jogador in self.__jogadores:
            if jogador.get_indice() == 1:
                jogador.set_turno(True)

    # Diz qunatas faz
    def diz_quantas_faz(self):
        self.__rodada.diz_quantas_faz()

    # Jogar carta
    def jogar_carta(self):
        self.__rodada.jogar_carta()

        # Verificar fim de jogo
        if self.__rodada.terminou():
            if self.__numero_da_rodada == 7:
                self.__player_interface.set_fim_de_jogo()
            else:
                self.criar_rodada()
    
    # Criar nova rodada
    def criar_rodada(self):
        self.__numero_da_rodada += 1
        self.__rodada = Rodada(self.__player_interface, self.__jogadores, self.__numero_da_rodada)



        
        