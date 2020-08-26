class Persona():

    def __init__(self, nombre):
        self.nombre = nombre

    def avanza(self):
        print(f'Ando caminando')

class Ciclista(Persona):

    def __init__(self, nombre):
        super().__init__(nombre)

    def avanza(self):
        print(f'Ando en bici')
        # return super().avanza()


def main():
    perso = Persona('David')
    perso.avanza()

    cicl = Ciclista('Dan')
    cicl.avanza()


if __name__ == "__main__":
    main()