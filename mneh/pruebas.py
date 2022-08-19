nombre = 'Ñasaindy'
apellido = 'Ñaño'
i = 0
letraBasada = ['Ñ','ñ']

while (i < len(letraBasada)):

    if(letraBasada[i] in nombre):
        indx = nombre.index(letraBasada[i])
        nombre[indx].replace('Ñ','n')
        print(nombre)

    else:
        if(letraBasada[i] == apellido):
            print(nombre.index(letraBasada[i]))
            print('apellido')

    i+=1
