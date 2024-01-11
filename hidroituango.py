#CONDICIONES MULTIPLES 

sensorNivelAgua=int(input('Digite el nivel de agua de una represa: '))

if sensorNivelAgua > 0 & sensorNivelAgua < 150:
    print('La represa tiene POCA agua: ')
elif sensorNivelAgua < 100:
    print('La represa esta NORMAL de agua: ')    