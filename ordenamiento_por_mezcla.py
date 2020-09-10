import random

def ordenamiento_por_mezcla(lista):
    
    if len(lista) > 1:

        mitad = len(lista) // 2
        izquierda = lista[:mitad]
        derecha = lista[mitad:]

        print(izquierda, '*'*5, derecha)
        # Llama recursiva a las mitades
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)

        # Comparaciones

        # iteradores para las sublistas
        i = 0
        j = 0

        # interadoes para la lista principal
        k = 0

        while i < len(izquierda) and j < len(derecha):
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
            else:
                lista[k] = derecha[j]
                j += 1
            
            k += 1
        
        while i < len(izquierda):
            lista[k] = izquierda[i]
            k += 1
            i += 1

        while j < len(derecha):
            lista[k] = derecha[j]
            k += 1
            j += 1
        
        print(f'izquierda {izquierda} derecha {derecha}')
        print(lista)
        print('-' * 50 )
    return lista



if __name__ == "__main__":
    tamano_de_lista = int(input('Tamaño de la lista? '))

    lista = [random.randint(0,100) for i in range(tamano_de_lista)]
    print(lista)

    lista_ordenada = ordenamiento_por_mezcla(lista)
    print('-'*80)
    print(lista_ordenada)