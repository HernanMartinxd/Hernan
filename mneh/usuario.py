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

    def ArreglarNombreyApellido(self):
        self.__apellido = string.capwords(self.__apellido)
        self.__nombre = string.capwords(self.__nombre)
    
    def SacarGuionesYpuntosDNI(self):
        if('-' in self.__dni):
            aux = self.__dni.split('-')
            aux = ''.join(aux)
            self.__dni = aux
    
    

