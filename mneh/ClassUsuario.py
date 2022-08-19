import string
class Usuario:
    __email = ''
    __nombre = ''
    __apellido = ''
    __clave = 0
    __numTelefono = 0
    __plathform = 'plathform'
    __departamento = ''

    def __init__(self,apellido,nombre,email,dni,numTelefono,departamento):
        self.__email = email
        self.__nombre = nombre
        self.__apellido = apellido
        self.__departamento = departamento
        self.__clave = 0
        self.__plathform
        self.__numTelefono = numTelefono

    #Arreglar Datos
    def ArreglarNombreyApellido(self):
        self.__apellido = string.capwords(self.__apellido)
        self.__nombre = string.capwords(self.__nombre)
    
    def SacarGuionesYpuntosDNI(self):
        if('-' in self.__dni):
            aux = self.__dni.split('-')
            aux = ''.join(aux)
            self.__dni = aux
        elif('.' in self.__dni):
            aux = self.__dni.split('-')
            aux = ''.join(aux)
            self.__dni = aux

    def validarCorreo(self):
        dominios = ['gmail.com','hotmail.com','icloud.com','outlook.com']
        aux = self.__email.split('@')
        i = 0
        band = False 

        while(not band):
    
            if(dominios[i] == aux[1]):
                print(dominios[i])
                band = True
            else:
                i+=1   #Queda pendiente realizar el procedimiento de eliminacion cuando ningun dominio coincide con el correo del usuario

    def QuitarLetraBasada(self):
        i = 0
        letraBasada = ['Ñ','ñ']

        while (i < len(letraBasada)):

            if(letraBasada[i] in self.__nombre):
                print(self.__nombre.index(letraBasada[i]))
                print(nombre)
                
            else:
                if(letraBasada[i] == self.__apellido):
                    print(nombre.index(letraBasada[i]))
                    
            i+=1

    def PonePassword(self):
        pass

    def CompletaConDatos(self):
        pass

    def CrearCodigoYAsignarCurso(self):
        pass


