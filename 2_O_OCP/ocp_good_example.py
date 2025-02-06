from abc import ABC, abstractmethod

class AprovadorExame(ABC):
    @abstractmethod
    def aprovar_solicitacao_exame(self, exame):
        pass
    
    @abstractmethod
    def verificar_condicoes_exame(self, exame):
        pass

class AprovadorExameSangue(AprovadorExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verificar_condicoes_exame(exame):
            print('Exame de sangue aprovado')

    def verificar_condicoes_exame(self, exame):
        pass

class AprovadorExameRaioX(AprovadorExame):
    def aprovar_solicitacao_exame(self, exame):
        if self.verificar_condicoes_exame(exame):
            print('Exame de Raio-X aprovado')

    def verificar_condicoes_exame(self, exame):
        pass

class Exame:
    def __init__(self, tipo):
        self.tipo = tipo

aprovador_exame_sangue = AprovadorExameSangue()
aprovador_exame_raio_x = AprovadorExameRaioX()

exame_sangue = Exame('sangue')
exame_raio_x = Exame('raio-x')

aprovador_exame_sangue.aprovar_solicitacao_exame(exame_sangue)
aprovador_exame_raio_x.aprovar_solicitacao_exame(exame_raio_x)