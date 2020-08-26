import random

def busqueda_binaria(lista, comienzo, final, objetivo, int_bin=0):
    #print(f'Buscando {objetivo} entre {lista[comienzo]} y {lista[final-1]}')
    
    int_bin+=1

    if comienzo > final:
        return (False, int_bin)
    
    medio = (comienzo+final) // 2

    if lista[medio]== objetivo:
        return (True,int_bin)
    elif lista[medio] < objetivo:
        return  (busqueda_binaria(lista,medio+1,final, objetivo, int_bin))
    else:
        #if lista[medio] > objetivo:
        return (busqueda_binaria(lista,comienzo,medio-1, objetivo ,int_bin))
   
def busqueda_lineal(lista, objetivo, int_lin=0):
    match = False

    for elemento in lista:  # O(n)
        int_lin+=1
        if elemento == objetivo:
            match = True
            break
    return (match, int_lin)
    
    

if __name__ == "__main__":
    
    tamano_lista = int(input('Tamanho de la lista? '))
    objetivo = int(input('Que numero deseas encontrar? '))

    lista = [random.randint(0,100) for i in range(tamano_lista)]

    (encontrado,int_bin) = busqueda_binaria(sorted(lista), 0, len(lista), objetivo)
    (encontrado,int_lin) = busqueda_lineal(lista, objetivo)
    #print(lista)
    print(f'El elemento: {objetivo}  {"esta" if encontrado else "no esta"}')
    print(f'interaciones lineal: {int_lin}')
    print(f'interaciones binary: {int_bin}')
    