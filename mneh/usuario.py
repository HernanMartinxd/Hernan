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
