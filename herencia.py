

class Rectangulo:

    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    
    def area(self):
        return self.base * self.altura

class Cuadrado(Rectangulo):
    
    def __init__(self, lado):
        super().__init__(lado, lado)

if __name__ == "__main__":
    rectan = Rectangulo(2,3)

    cuadra = Cuadrado(2)

    print(f'Area Rect { rectan.area() } Area Cuadrado: {cuadra.area()}')