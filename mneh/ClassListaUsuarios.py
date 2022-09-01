from ClassUsuario import Usuario
from datetime import datetime
import csv

class ListaUsuarios:

    __list = []
    def __init__(self):
        self.__list = []

    def AgregarUser(self,usr):
        self.__list.append(usr)

    def probarMetodo1(self):  # Testeado - Funciona 1

        for obj in self.__list:
            obj.ArreglarNombreyApellido()

    def probarMetodo2(self):  # Testeado - Funciona 2

        for obj in self.__list:
            obj.SacarGuionesYpuntosDNI()

    def probarMetodo3(self):  # Testeado - Funciona 3

        for i in range(len(self.__list)):
            self.__list[i].PonePassword()
            print('Password: {} usuario: {}'.format(
                self.__list[i].getClave(), self.__list[i].getNombre()))

    def probarMetodo4(self):  # Testeado - Funciona 4
        i = 0
        j = 0
        cantSimilitudes = []
        while (i < len(self.__list)):
            j = i+1

            while (j < len(self.__list)):
                if (self.__list[i] == self.__list[j]):
                    print('Se encontro un duplicado {} == {}'.format(
                        self.__list[i].getNombre(), self.__list[j].getNombre()))
                    cantSimilitudes.append(self.__list.index(self.__list[i]))
                j += 1
            i += 1
        cnj = set(cantSimilitudes)
        cnj = list(cnj)

        for i in cnj:
            self.__list.pop(i)

    def probarMetodo4(self): #Testeado - Funciona 5
        
        for i in range(len(self.__list)):
            self.__list[i].CrearCodigoYAsignarCurso()

    def probarMetodo5(self):

        for i in range(len(self.__list)):
            print('Nombre: {} - Apellido: {}'.format(self.__list[i].getNombre(),self.__list[i].getApellido()))

    def probarMetodo6(self):
        f = datetime.now()

        nombre = 'C:/Users/herna/Desktop/Archivos CSV usuarios/Archivo Usuarios ' + f.strftime("%M-%Y %h-%m") + '.csv'

        nombre = 'pr/Archivo Carga ' + f.strftime("%M-%Y %h-%m") + '.csv'

        list = []
        for i in range(len(self.__list)):
            list.append(self.__list[i].getDatos())

        with open(nombre,'w+',encoding = 'utf-8') as file:
            writer = csv.writer(file)

            for elem in list:
                writer.writerow(elem)    

        with open(nombre,'w+',encoding = 'utf-8') as file:
            writer = csv.writer(file)

            for elem in list:
                writer.writerow(elem)    

