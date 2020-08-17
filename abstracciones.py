class Lavadora:

    def __init__(self):
        pass

    def lavar(self, temperatura='caliente'):
        self._llenar_tanque_de_agua(temperatura)
        self._anadir_jabon()
        self._lavar()
        self._centrifugar()

    def _llenar_tanque_de_agua(self, temperatura):
        print(f'Llenando el tanque de agua {temperatura}')

    def _anadir_jabon(self):
        print(f'Agregando agua al tanque')

    def _lavar(self):
        print(f'Lavando ropa')
    
    def _centrifugar(self):
        print(f'Secando ropa')


if __name__ == "__main__":
    lavadora = Lavadora()
    print(lavadora.lavar())