'''
Challenge 4: Encuentra la contraseña de tu amigo

Problema

Un amigo compró 5 BitCoins en 2008. El problema es que lo tenía en un monedero digital... ¡y no se acuerda de la contraseña!

Nos ha pedido ayuda. Y nos ha dado algunas pistas:

- Es una contraseña de 5 dígitos.
- La contraseña tenía el número 5 repetido como mínimo dos veces.
- El número a la derecha siempre es mayor o igual que el que tiene a la izquierda.

Nos ha puesto algunas ejemplos:
55678 es correcto lo cumple todo
12555 es correcto, lo cumple todo
55555 es correcto, lo cumple todo
12345 es incorrecto, no tiene el 5 repetido.
57775 es incorrecto, los números no van de forma creciente

Dice que el password está entre los números 11098 y 98123. ¿Le podemos decir cuantos números cumplen esas reglas dentro de ese rango?

Cómo enviar la solución
Envía la solución con el comando submit, y el número de passwords que cumplen el criterio junto con el password que está en el índice 55 
de la lista de passwords válidos, separado por un guión.

Por ejemplo, para 87 resultados y el password 35522 en la posición 55 sería:

$ submit 87-35522'''
import time

def timer(function):
    def wrapper(*args,**kwargs):
        start = time.time()
        result = function(*args,**kwargs)
        end = time.time()
        print(function.__name__, f"was run in {end-start:.3f} seconds")
        return(result)
    return wrapper


@timer
def password(fr, to):
    opts = []
    for opt in range(fr,to):
        before = int(str(opt)[0])
        res = 0
        reps = 1 if int(str(opt)[0]) == 5 else 0
        for i in range(1,5):
            if before <= int(str(opt)[i]):
                before = int(str(opt)[i])
                res += 1                
            if int(str(opt)[i]) == 5:
                reps += 1
            
            if res == 4 and reps >= 2:
                opts.append(opt)

    return opts
    
# print(f"submit {len(password(11098,98123))}-{password(11098,98123)[55]}")
print(password(11098,20000))
