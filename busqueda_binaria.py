obj = int(input('Num: '))
epsilon = 0.0001
limit_inferior = 0.0
limit_superior = max(1.0, obj)
resp = (limit_superior +limit_inferior) / 2

while abs(resp**2 - obj) >= epsilon:
    print(f'resp: {resp} - lim_inf: {limit_inferior} - lim_sup: {limit_superior} - **2 {resp**2}')
    if (resp**2 < obj ):
        limit_inferior = resp
    else:
        limit_superior = resp
    resp = (limit_superior +limit_inferior) / 2

print(f'la raiz cuadrada: {resp}')