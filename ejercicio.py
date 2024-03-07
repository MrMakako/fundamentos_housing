##lista=["append",2,"hola"]
lista_numeros=[1,10,11]
palabra="Hola"
lista_2d=[["Jueves","Viernes","Sabado"],["Martes","Lunes","Domingo"]]
nombres=["Juna", "Ana","Guillermo","Lorenzo","Ana","Guillermo"] 



def buscar_numero(numero):
    for n in lista_numeros:
        if(n==numero):
            return True
    return False

def buscar_palabra(palabra):
    for n in nombres:
        if(n.lower()==palabra.lower()):
            return True
    return False


def revisar_duplicas(lista_i,list_size):
    for n in range(0,list_size):
        elemento=lista_i[n]
        for x in range(n,list_size):
            if(elemento==lista_i[x]):
                print(x)
                print(n)






nombres.remove("Ana")
nombres.pop(0)
lista_numeros.pop(0)
lista_numeros.remove(11)

print(nombres)
print(lista_numeros)
