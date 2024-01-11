#PERRO NEGRO

nombre = input('Dame Tu Nombre:')
paisCliente = input('De Donde Eres?:')
cantidadPersonas = int(input('Cuantas Personas Van A Reservar?:'))
añoNacimientoCliente = int(input('En Que Año Nacio?'))

#CALCULAR LA EDAD DEL CLIENTE

añoActual = 2024
edadCliente = añoActual - añoNacimientoCliente

#CLASIFICAR, PREGUNTAR, DECIDIR 

if edadCliente >= 18:
    print('Puedes Entrar')
else:
    print('Ve Pa Tu Casa')