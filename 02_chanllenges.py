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
        return print("They are the same word")
    elif sorted(frs_str) == sorted(sec_str):
        return print("It is an anagram")
    else:
        print("It isn't an anagram")

is_anagram("the alias men","Alan Smithee")
is_anagram("RoMa","amor")
is_anagram("hola","H o L a")
is_anagram("rng","rlg")

'''
This Python function 'is_anagram(frs_str, sec_str)' is designed to determine whether two strings are 
anagrams of each other. An anagram is a word or phrase formed by rearranging the letters of another 
word or phrase.

Here's the breakdown of how this function works:

-  'frs_str': Represents the first string input.
-  'sec_str': Represents the second string input.
-  'frs_str.lower().replace(" ", "")': This line converts the first string to lowercase using the 'lower()' 
   method and removes spaces using the 'replace()' method.
-  'sec_str.lower().replace(" ", "")': This line does the same for the second string.
After removing spaces and converting both strings to lowercase, the function checks for three conditions:

1.  If the modified versions of the two strings are the same, it means they are identical strings. In this 
    case, it prints "They are the same word".
2.  If the sorted characters of both strings are equal, it means they contain the same characters and thus
    are anagrams of each other. In this case, it prints "It is an anagram".
3.  If none of the above conditions are met, it means the strings are neither identical nor anagrams of each 
    other. In this case, it prints "It isn't an anagram".
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
"""
This Python function 'palindromo(string)' is designed to determine whether a given string is a palindrome. 
A palindrome is a word, phrase, number, or other sequence of characters that reads the same forward and backward.
Here's a breakdown of how this function works:
-   'string': Represents the input string to check for palindrome.
-   'string.lower().replace(" ", "").replace(",", "")replace("/","")': This line converts the input string to 
    lowercase using the 'lower()' method and removes spaces, slash and commas using the 'replace()' method.
After removing spaces and commas and converting the string to lowercase, the function checks if the modified 
string is equal to its reverse:
1.  'string[::-1]': This syntax '[::-1]' is used to reverse the string. It creates a new string with characters 
    in reverse order.
2.  If the original string is equal to its reverse, it means the string reads the same forward and backward, 
    making it a palindrome. In this case, it prints "Es un palindromo".
3.  If the original string is not equal to its reverse, it means the string is not the same forward and 
    backward, indicating it is not a palindrome. In this case, it prints "No es un palindromo".
"""
#_____________________________________________________________________________________________________________

#Fibonacci
"""
#3
LA SUCESIÓN DE FIBONACCI
/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

def fibonacci():
   prev = 0
   next = 1
   for i in range(0,10):
       print(prev)
       fib = prev + next
       prev = next
       next = fib
fibonacci()

def fibonacci(n):
    prev = 0
    next = 1
    while prev<n:
        print(prev)
        fib = prev+next
        prev = next
        next = fib
fibonacci(10)

#forma compacta
def fibonacci(n):
    prev , next = 0 , 1
    while prev<n:
        print(prev)
        prev , next = next , prev + next
fibonacci(10)

#_____________________________________________________________________________________________________________

"""
¿ES UN NÚMERO PRIMO?
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 * Un número primo es un número natural positivo mayor que 1 que solo es divisible entre si mismo y 1.
 */
"""

def is_prime_boolean(n):
        for i in range(2,n):
            if n % i == 0:
                return False
        return True 
print(is_prime_boolean(2))
"""
This function "is_prime_boolean" takes a single parameter "n", which presumably represents an integer. 
Its purpose is to determine whether "n" is a prime number or not. Here's how it works:
1.  The function starts by iterating through a range of numbers from 2 to "n-1" using a for loop. This 
    loop is used to check if "n" is divisible by any number other than 1 and itself.
2.  Inside the loop, for each "i" in the range, it checks if "n" is evenly divisible by "i" ("n % i == 0"). 
    If it is, it means "n" is divisible by a number other than 1 and itself, which means it's not a prime 
    number, and the function returns "False".
3.  If the loop completes without finding any number that "n" is divisible by, the function returns
    "True", indicating that "n" is indeed a prime number since it's only divisible by 1 and itself.

In summary, this function takes an integer "n" as input and returns "True" if "n" is a prime 
number, and "False" otherwise. It uses a simple algorithm of checking divisibility by all numbers 
from 2 to "n-1". If "n" is divisible by any of these numbers, it's not a prime, otherwise, it's prime.
"""

def is_prime(n):
    if n <= 1:
        print(f"{n} no existen primos menores a 2")
    elif is_prime_boolean(n) == True:
        print(f"{n} es primo")
    else:
        print(f"{n} no es primo")

def prime_before(m):
    n = 2
    while n <= m:
        if is_prime_boolean(n) == True:
            print(n)
        else:
            pass
        n = n + 1
prime_before(100)

def frst_n_primes(m):
        n = 2
        i = 1
        while i <= m:
            if is_prime_boolean(n) == True:
                print(n)
                i = i + 1
                n = n + 1
            else:
                n = n + 1
frst_n_primes(25)
"""
This Python function "frst_n_primes(m)" is designed to print the first "m" prime numbers. Let's break 
down how it works:

1.  "n = 2": This line initializes a variable "n" to 2. "n" will represent the numbers that we will check 
    for primality starting from 2.

2.  "i = 1": This line initializes a variable "i" to 1. "i" will keep track of the number of prime numbers 
    found so far.
3.  "while i <= m:": This line starts a while loop that continues as long as the count of prime numbers 
    found ("i") is less than or equal to the total number of primes required ("m").
4.  Inside the loop, "if is_prime_boolean(n) == True:": This line checks if the current value of "n" is a 
    prime number by calling the "is_prime_boolean()" function. If it returns "True", it means "n" is prime.
5.  If "n" is prime, "print(n)": This line prints the prime number.
6.  "i = i + 1": This line increments the count of prime numbers found ("i") by 1.
7.  "n = n + 1": This line increments "n" by 1, so the loop will move on to the next number for 
    checking primality.
8.  If the current value of "n" is not prime, it simply increments "n" by 1 and moves to the next number to check.
9.  Once the loop completes ("i" reaches "m"), the function ends, having printed the first "m" prime numbers.

Overall, this function effectively finds and prints the first "m" prime numbers by iteratively checking each 
number starting from 2 until it has found "m" primes.
"""


