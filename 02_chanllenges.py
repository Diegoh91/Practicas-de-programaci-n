### Challenges ###

#_____________________________________________________________________________________________________________

### Recursividad ###
"""
/*
 * EJERCICIO:
 * Entiende el concepto de recursividad creando una función recursiva que imprima
 * números del 100 al 0.
 *
 * DIFICULTAD EXTRA (opcional):
 * Utiliza el concepto de recursividad para:
 * - Calcular el factorial de un número concreto (la función recibe ese número).
 * - Calcular el valor de un elemento concreto (según su posición) en la 
 *   sucesión de Fibonacci (la función recibe la posición).
 */
"""

#ej 1:
#countDown whit while:

def countDown(n):
    try:          
        while n>=0:     #while n is greater or equal than zero
            print(n)    #print n
            n=n-1       #changes n to n-1
    except:
         print("the program only admits int values")
countDown()

'''
¿Como funcuiona este programa?
Tenemos que saber que:
    1)_ el comando while va a repetir el programa hasta que se cumpla la condición puesta luego del mismo
    2)_ el try y el except solo se pusieron para casos donde no ingresen valores de tipo int (no es relevante)
Sabiendo esto el programa hace lo siguiente:
    1)_ Mientras que n sea mayor o igual a 0, va a imprimir n y luego le va a restar 1 antes de repetir el 
        programa hasta llegar a n=0
    2)_ el comando try va a intentar ejecutar el comando while, si es que no se puede, por ejemplo si ponemos
        un string, nos va a retrornar el except.
'''  

#Count Down whitout while:

def otherCountDown(n):
    try:
        if n==0:                      #if n equal to zero
            print(n)                  #print n
        elif n<0:                     #if n less than zero, print
            print("the program needs values greater than zero")
        else:                         #else
            print(n)                  #print n
            otherCountDown(n-1)       #execute otherCountDown with n-1
    except:
        print("the program only admits int values")
otherCountDown()

'''
¿Como funcuiona este programa?
Tenemos que saber que:
    1)_ if verifica condiciones
    2)_ elif es lo mismo que el if, pero jerarquicamente debajo del if
    3)_ else es el caso cuando con son verdaderas ni las condiciones del if y el elif
Sabiendo esto el programa hace lo siguiente:
    1)_ if n es igual a 0, entonces imprime n, esto significa que cuando lleguemos a 0, termina el programa.
    2)_ elif n es menor que cero, no podemos hacer una cuenta regresiva, por lo que nos lo informa.
    3)_ else si no se cumplen ni el if y el elif, entonces imprime n y vuelve a ejecutar el programa con 
        el valor de n restado 1 y así hasta que n es igual a 0 y se finaliza el programa con el if inicial.
''' 
        
#Factorial program:

def factorialFunction(n):
    try:
        if n==0:                                                        #if n equal zero
            return 1                                                    #return 1
        elif n<0:                                                       #if n less than zero
            print("the program only admits values greater than zero")   #print
        else:                                                           #else n greater than zero
            return n*factorialFunction(n-1)                             #return n times factorialfunction
    except:
        print("the program only admits int values")
def factorial(n):
    print(factorialFunction(n))
factorial(3)

'''
¿Como funciona el programa?
Tenemos que saber que:
    1)_ if verifica condiciones
    2)_ elif es lo mismo que el if, pero jerarquicamente debajo del if
    3)_ else es el caso cuando con son verdaderas ni las condiciones del if y el elif
Sabiendo esto, el programa hace lo siguiente:
    1)_ if verifica si n es igual a 0 y si es verdadero imprime 1, puesto que el factorial de 0 es 1
        y termina el programa (no es necesario hacer mas por como es la función factorial)
    2)_ elif verifica que n no sea negativo, puesto que no tenemos forma de calcular factoriales negativos
        (o si? eso se lo dejamos a los matemáticos, ellos tambien calculan factoriales de floats)
    3)_ else si no se cumplen ninguna de las condiciones anteriores, entonces retornaremos el valor de 
        n multiplicado por el resultado del programa en n-1 y así hasta que n sea = 0 y haga esa 
        ultima multiplicación por el if.
Por ejemplo:
    si n = 3, el factorial sería 3*2*1 y el programa lo calcula de la siguiente forma:
    1)_ if Verifica que 3 == 0, como esto es falso va a la siguiente linea de código donde verifica
        si 3 < 0, como esto es falso, pasa a la siguiente linea de código donde retronará el valor
        3*factorial(2) y ¿cuando vale 3*factorial_function(2)? Bueno, el programa se vuele a ejecutar
        haciendo nuevamente las verificaciones y determinando que tiene que hacer 3*2*factorial_function(1)
        y vuelve a ejecutarse devolviendo 3*2*1*factorial_function(0) que por el if da 1 y termina la
        ejecución del programa, devolviendo la cadena recursiva 3*2*1*0! = 6 (el 0! significa en matematicas
        "cero factorial", que bueno, es igual a 1) 
'''

#_____________________________________________________________________________________________________________
"""
El famoso "FIZZ BUZZ"
Escribe un programa que mestre por consola (con un print) los numeros
del 1 al 100 (ambos incluidos con un salo de linea ntre cada
impresión, sustituyendo por los siguientes:
-multiplos de 3 por la palabra "fizz".
-multiplos de 5 por la palabra "buzz".
-multiplos de 3 y de 5 por la palabra "fizzbuzz"
"""

def fizz_buzz(m,n):
    for i in range(m,n+1): 
        if i % 3 == 0 and i % 5 ==0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)
fizz_buzz(1,15)

'''
Que es lo que hace el programa?
Que tenemos que saber:
1)_ la función % "modulo" divide un numero y entre otro numero y retorna el resto de la divición, como 
    queremos saber multiplos, esto implica que la divición da como resto 0.
2)_ el conector "and" une 2 condiciones dentro de un condicional como el if o el elif exigiendo que ambas
    se cumplan en simultaneo
3)_ para hacer el loop que genere los elementos es necesario usar un for i in range(inicio,fin+1)
    de modo que puedas ir verificando las condiciones de cada uno de los elementos creados en ese rango
    a travez de los if y elif
4)_ como trabajamos con una jerarquia en los comandos, no podríamos poner el doble condicional abajo,
    porque el doble condicional es una union de 2 condiciones por separado y si pusieramos primero
    una de las condiciones por separado, tomaría primero la concición por separado y no llegaría nunca
    al doble condicional.
'''

#Otra forma de construir un programa que haga lo mismo pero con un while:
#con este podemos preguntar en diferentes rangos como se vería el programa
def fizz_buzz(n,m):
    while n<=m:
        if n % 3 == 0 and n % 5 == 0:
            print("fizzbuzz")
        elif n % 3 == 0:
            print("fizz")
        elif n % 5 == 0:
            print("buzz")
        else:
            print(n)
        n = n + 1
fizz_buzz(1,100)
'''
¿Como funciona este otro programa?
Este prgrama cumple la misma funcion pero con otro metodo, a travez de un while.
Que tenemos que saber:
    1)_ la funcion while repetira el programa hasta que se cumpla la condicion del mismo
    2)_ es importante el orden jerarquico con el que se escriben los condicionales
Sabiendo esto, el programa hace lo siguiente:
    1)_ el programa recibe 2 parametros que son los valores entre los que verificara las condiciones
    3)_ el comado % devuelve el resto de la division entre 2 valores int.
    2)_ una ves ingresados los parametros, el programa va a ingresar por el while con la condicion 
        de que n sea menor o igual a m y se volverá a ejecutar aumentando n+1 cada vez que se ejecuta 
        hasta que n sea igual a m donde el programa se dentendra
    3)_ en cada ejecucion, el programa primero revisar el condicional if donde verificara en simultaneo las
        condiciones de: if el resto de la division entre 3 da resto 0 y la division entre 5 da resto 0, lo 
        que implicaría que el numero es multiplo de 3 y de 5 en simultaneo e imprime "fizzbuzz", si esta 
        condicion no se cumple pasa a la siguiente linea de codigo donde verifica si el resto de la division
        entre el numero y 3 da 0, lo que implica que es multiplo solamente del 3 e imprime "fizz", si esta 
        condicion no se cumple pasa a la siguiente linea de codigo donde verifica si el resto de la division
        entre el numero y 5 da cero, lo que implicaría que el numero es multiplo de 5 e imprime "buzz"
        finalmente, si no se cumple niguna condicion, el programa va por el else donde imprime el numero.
'''

#_____________________________________________________________________________________________________________

#Es un anagrama?
"""
/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""

def is_anagram(frs_str,sec_str):
    frs_str=frs_str.lower().replace(" ","")
    sec_str=sec_str.lower().replace(" ","")
    if frs_str  == sec_str :
        return print("Son la misma palabra")
    elif sorted(frs_str) == sorted(sec_str):
        return print("Es un anagrama")
    else:
        print("No es un anagrama")

is_anagram("the alias men","Alan Smithee")
is_anagram("RoMa","amor")
is_anagram("hola","H o L a")
is_anagram("rng","rlg")

'''

'''

#_____________________________________________________________________________________________________________

#Es un palidromo?:
"""
"""

def palidromo(string):
    string = string.lower().replace(" ","").replace(",","")
    if string == string[::-1]:
        print("Es un palidromo")
    else:
        print("No es un palidromo")
palidromo("Neuquen")
palidromo("quena")
palidromo("Adan no cede con Eva y Yave no cede con nada")
palidromo("Red rum, sir, is murder")

