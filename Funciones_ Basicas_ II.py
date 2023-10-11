#1
def countdown(numero):
    
    lista_cuenta_regresiva = []
    
    for i in range(numero, -1, -1):
        
        lista_cuenta_regresiva.append(i)
    
    return lista_cuenta_regresiva

resultado = countdown(10)
print(resultado)

#2

def imprime_y_devuelve(numero):

    lista_imprime_devuelve = [3,4]

    if numero == 3:
        return 3 
    return 4 

resultado = imprime_y_devuelve(3)
print(resultado)

#3
def suma_primero_mas_longitud(lista):
    if not lista: 
        return 0
    else:
        return lista[0] + len(lista)

mi_lista = [1, 2, 3, 4, 5]
resultado = suma_primero_mas_longitud(mi_lista)
print(resultado) 

#4
def valores_mayores_que_el_segundo(lista):
    if len(lista) < 2:
        return False

    segundo_valor = lista[1]
    valores_mayores = [valor for valor in lista if valor > segundo_valor]

    print(len(valores_mayores))
    return valores_mayores

lista1 = [5, 2, 3, 2, 1, 4]
resultado1 = valores_mayores_que_el_segundo(lista1)
print(resultado1)  

lista2 = [3]
resultado2 = valores_mayores_que_el_segundo(lista2)
print(resultado2) 

#5

def length_and_value(tamaño, valor):
    lista = [valor] * tamaño
    return lista

resultado1 = length_and_value(4, 7)
print(resultado1)  

resultado2 = length_and_value(6, 2)
print(resultado2)  

