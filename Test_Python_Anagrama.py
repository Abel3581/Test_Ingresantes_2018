
def cantAnagramasEnCadena(cadena, propuesta):
    cantAnagramas=0
    listaLetras=[]
    for caracter in cadena:
        if letraEstaEnCadena(caracter, propuesta):
            listaLetras.append(caracter)

        if mismoTamaño(listaLetras, propuesta):
            cantAnagramas=cantAnagramas+1
            listaLetras=[]


    return cantAnagramas


def letraEstaEnCadena(caracter, cadena):
    return caracter in cadena

def mismoTamaño(lista, cadena):
    return len(lista) == len(cadena)


def esAnagramaParcial(lista, propuesta):
    #Transformamos el string propuesto en una lista

    listaPropuesta=[]
    for letra in propuesta:
        listaPropuesta.append(letra)

    # Verificamos si todos los caracteres de la lista estan en la propuesta. de ser asi retorna true

    for char in lista:
        if char not in listaPropuesta:
            return False

        lista.remove(char)
        listaPropuesta.remove(char)
    return True


print(cantAnagramasEnCadena("hola, que buena ola Laomir", "oal"))






##Buscando anagramas

##  Se provee una cadena de caracteres de largo N y una subcadena de largo M. Se desea saber
##  cuántas veces aparece la subcadena o un anagrama de la misma dentro de la cadena principal.
##  Por ejemplo, si se tiene la cadena A y la subcadena B
##  A = “hola, que buena ola Laomir”
##  B = “OAL”
##  El resultado deberá ser 3, dado lo siguiente
##  A = “hola, que buena ola Laomir”
##  Escribir una función
##  Int solution(string A, string B)
##  que devuelva la cantidad de veces que aparece B en A, o un anagrama de B en A.
##  Asumir:
##  No hay distinción entre mayúsculas y
##  minúsculas N > M.

