import random

def ordenamiento_de_insercion(lista):
    n = len(lista) # Tamaño de la lista

    for i in range(1, n):
        valor_actual = lista[i] 
        posicion_actual = i
        posicion_izq = posicion_actual - 1
        print(f'posicion_actual: {posicion_actual} lista[posicion_izq]: {lista[posicion_izq]} valor_actual: {valor_actual}')
        while posicion_actual > 0 and lista[posicion_izq] > valor_actual:
            
            print(f'Ordenando: posicion_actual: {posicion_actual} posicion_izq: {posicion_izq} valor_actual: {valor_actual}')

            lista[posicion_actual] = lista[posicion_izq]
            posicion_actual -= 1
            posicion_izq = posicion_actual - 1
        
        lista[posicion_actual] = valor_actual
        print(f'posicion_actual: {posicion_actual}, {lista}')
        
            
        # for j in range(len(sublista_ordenada)):

        #     print(f'Dentro de 2do for: {lista[i]} y {sublista_ordenada[j]}')
        #     if lista[i]>sublista_ordenada[j]:
        #         print(f'Dentro de condicion: ${lista[i]} y ${sublista_ordenada[j]}')
                # lista[i], sublista_ordenada[j]  = sublista_ordenada[j], lista[i]
        
        # for j in range(0, n-i-1): # tamaño de la lista menos lo ya recorrido menos uno 
            
        #     if lista[j] > lista[j+1]:
        #         lista[j], lista[j+1] = lista[j+1], lista[j]
            
    return lista


if __name__ == "__main__":
    tamano_de_lista = int(input('Tamaño de la lista? '))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_de_insercion(lista)
    print(lista_ordenada)