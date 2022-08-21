from ClassUsuario import Usuario
import csv

class ListaUsuarios:

    def __init__(self):
        self.__list = []
        file = open('datos.csv')
        reader = csv.reader(file, delimiter = ',')

        for fila in reader:
            obj = Usuario(fila[1],fila[2],fila[3],fila[4],fila[5],fila[7])
            self.__list.append(obj)


    def probarMetodo1(self): #Testeado - Funciona 1

        for obj in self.__list:
            obj.ArreglarNombreyApellido()

    def probarMetodo2(self): #Testeado - Funciona 2
        
        for obj in self.__list:
            obj.SacarGuionesYpuntosDNI()

    def probarGeneradorDeClaves(self): #Testeado - Funciona 3

        for i in range(len(self.__list)):
            self.__list[i].PonePassword()
            print('Password: {} usuario: {}'.format(self.__list[i].getClave(),self.__list[i].getNombre()))
            
    def BuscarYEliminarDuplicados(self): #Testeado - Funciona 4
        i = 0 
        j = 0
        cantSimilitudes = []
        while(i < len(self.__list)):
            j = i+1

            while(j < len(self.__list)):
                if(self.__list[i] == self.__list[j]):
                    print('Se encontro un duplicado {} == {}'.format(self.__list[i].getNombre(),self.__list[j].getNombre()))
                    cantSimilitudes.append(self.__list.index(self.__list[i])) 
                j+=1
            i += 1
        cnj = set(cantSimilitudes)
        cnj = list(cnj)
        print(len(self.__list))

        for i in cnj:
            self.__list.pop(i)



if __name__ == '__main__':
    obj = ListaUsuarios()
    obj.BuscarYEliminarDuplicados()
