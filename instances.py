class Coordenada:

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, otra_coordenada):
        x_diff = (self.x - otra_coordenada.x)**2
        y_diff = (self.y - otra_coordenada.y)**2

        return (x_diff + y_diff)**0.5


if __name__ == '__main__':
    coord1 = Coordenada(1,2)
    coord2 = Coordenada(3,4)

    print(coord1.distance(coord2))
    print(isinstance(coord1, Coordenada))
    print(isinstance(3, Coordenada))