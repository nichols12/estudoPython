class Terrestre:
    """
    Classe de veículos terrestres
    """
    se_move_em_terra = True
    def __init__(self, velocidade=100):
        """
        Inicializa o objeto
        """
        self.velocidade_em_terra = velocidade

class Aquatico:
    """
    Classe de veículos aquáticos
    """
    se_move_na_agua = True

    def __init__(self, velocidade=5):
        """
        Inicializa o objeto
        """
        self.velocidade_agua = velocidade

#A classe Carro deriva de terrestre
class Carro(Terrestre):
    """
    Classe de carros
    """
    roda = 4
    def __init__(self,velocidade=120,pistoes=4):

        self.pistoes = pistoes
        Terrestre.__init__(self,velocidade=velocidade)

#A classe barco deriva de Aquatico
class Barco(Aquatico):
    """
    Classe de Barcos
    """

    def __init__(self,velocidade=6, helices=1):
        """
        Inicializa o objeto
        """
        self.helices = helices
        Aquatico.__init__(self, velocidade=velocidade)

#A classe Anfibio é derivade de Carro e barco
class Anfibio(Carro,Barco):
    """
    Classe de anfíbios
    """
    def __init__(self,velocidade_em_terra=80, velocidade_na_agura=4, pistoes=6, helices=2):
        """
        Inicializa o objeto
        """
        # É preciso evocar o __initi__ de cada classe pai
        Carro.__init__(self,velocidade=velocidade_em_terra,pistoes=pistoes)
        Barco.__init__(self,velocidade=velocidade_na_agura,helices=helices)

novo_anfibio = Anfibio()
for atr in dir(novo_anfibio):
    #se não for um método especial:
    if not atr.startswith('__'):
        print(atr, '=' ,getattr(novo_anfibio, atr))
        