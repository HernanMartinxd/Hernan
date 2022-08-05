class Usuario:

    __email = ''
    __nombre = ''
    __apellido = ''
    __clave = 0
    __numTelefono = 0


    def __init__(email,nombre,apellido,clave,numTelefono):

        self.__email = email
        self.__nombre = nombre
        self.__apellido = apellido
        self.__clave = clave
        self.__numTelefono = numTelefono
