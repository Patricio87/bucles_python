# Bucles [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios con bucles "while"

# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea menor a 6>
# Además, complete la línea de código necesaria para que
# el valor de "x" incremente "1" en cada iteración

# reemplace "condicion" por lo que crea necesario

# Coloque la línea de código para que "x" incremente "1"

x = 0

i = False



while not i: 
    print ("Valor de x=", x)
    x += 1
    if x >= 6:
        break
        

    
    

   


# Dado el siguiente "while", complete la condicion
# para que el "while" itere siempre que <x sea mayor o igual a 0>
# Además, complete la línea de código necesaria para que
# el valor de "x" decremente "1" en cada iteración
# reemplace "condicion" por lo que crea necesario
# # Coloque la línea de código para que "x" decremente "1"
x = 5

while x >= 0:    
    print("Valor de x =", x)
    x-=1
    if x <= 0:
        break



print("terminamos!")
