class Supcl1:
    """
    Uma classe muito simples
    """
    varsup1 = 1

class Supcl2:
    """
    Outra classe muito Simples
    """
    varsup1 = 2

class Classe(Supcl1,Supcl2):
    """isto é uma classe queherda de Supcl1 e Supcl2"""
    clsvar = []

    def __init__(self,args):
        """
        Inicializador da classe
        """
        self.args = args

    def __done__(self):
        """
        Destrutor da classe
        """
        del self.args

    def metodo(self, params):
        """
        Método do objeto
        """
        self.args += params

    @classmethod
    def cls_metodo(cls,params):
        """
        Método de classe
        """
        cls.clsvar = params

    @staticmethod
    def est_metodo(params):
        """
        Método estático
        """
        return params

obj = Classe(0)
obj.metodo(-1)

Classe.cls_metodo(3)
Classe.est_metodo(4)
