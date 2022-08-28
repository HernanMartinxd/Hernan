from ClassUsuario import Usuario
import csv

class ListaUsuarios:

    def __init__(self):
        self.__list = []
        file = open('datos.csv')

        with open('datos.csv','r',encoding='utf-8') as file:
            reader = csv.reader(file)

            for fila in reader:    
                obj = Usuario(fila[1], fila[2], fila[3], fila[4], fila[5], fila[7])
                self.__list.append(obj)
        file.close()

    def probarMetodo1(self):  # Testeado - Funciona 1

        for obj in self.__list:
            obj.ArreglarNombreyApellido()

    def probarMetodo2(self):  # Testeado - Funciona 2

        for obj in self.__list:
            obj.SacarGuionesYpuntosDNI()

    def probarGeneradorDeClaves(self):  # Testeado - Funciona 3

        for i in range(len(self.__list)):
            self.__list[i].PonePassword()
            print('Password: {} usuario: {}'.format(
                self.__list[i].getClave(), self.__list[i].getNombre()))

    def BuscarYEliminarDuplicados(self):  # Testeado - Funciona 4
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

    def TestCodigoCurso(self): #Testeado - Funciona 5
        
        for i in range(len(self.__list)):
            self.__list[i].CrearCodigoYAsignarCurso()
            print(self.__list[i].getDepartamento())

    def MostrarDatosUsuarios(self):

        for i in range(len(self.__list)):
            print('Nombre: {} - Apellido: {}'.format(self.__list[i].getNombre(),self.__list[i].getApellido()))

        ''' #Mostrar todos los datos de los usuarios
        for i in range(len(self.__list)):
            print(self.__list[i])
            print('------------------------------------------------------')
           ''' 



if __name__ == '__main__':
    obj = ListaUsuarios()
    obj.probarMetodo1()
    obj.MostrarDatosUsuarios()
    print('vamo niubel')
