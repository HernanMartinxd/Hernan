import string


class Usuario:
    __email = ''
    __nombre = ''
    __apellido = ''
    __clave = ''
    __dni = ''
    __numTelefono = 0
    __plathform = 'plathform'
    __departamento = ''
    __status = ''

    def __init__(self, apellido, nombre, email, dni, numTelefono, departamento):
        self.__email = email
        self.__nombre = nombre
        self.__dni = dni
        self.__apellido = apellido
        self.__departamento = departamento
        self.__clave = 0
        self.__plathform
        self.__numTelefono = numTelefono
        self.__status = 'user'

    # Arreglar Datos
    def ArreglarNombreyApellido(self):
        self.__apellido = string.capwords(self.__apellido)
        self.__nombre = string.capwords(self.__nombre)

    def SacarGuionesYpuntosDNI(self):
        if ('-' in self.__dni):
            aux = self.__dni.split('-')
            aux = ''.join(aux)
            self.__dni = aux
        elif ('.' in self.__dni):
            aux = self.__dni.split('-')
            aux = ''.join(aux)
            self.__dni = aux

    def validarCorreo(self):
        dominios = ['gmail.com', 'hotmail.com', 'icloud.com', 'outlook.com']
        aux = self.__email.split('@')
        i = 0
        band = False

        while (not band):

            if (dominios[i] == aux[1]):
                print(dominios[i])
                band = True
            else:
                i += 1  # Queda pendiente realizar el procedimiento de eliminacion cuando ningun dominio coincide con el correo del usuario

    def QuitarLetraBasada(self):
        if (letraBasada1 in self.__nombre or letraBasada2 in self.__nombre):
            nuev = self.__nombre.replace('Ñ', 'N')
            nuev2 = nuev.replace('ñ', 'n')
            self.__nombre = nuev2

        if (letraBasada1 in self.__apellido or letraBasada2 in self.__apellido):
            nuevAp = apellido.replace('Ñ', 'N')
            nuevAp2 = nuevAp.replace('ñ', 'n')
            self.__apellido = nuev2

    def PonePassword(self):
        self.__clave = self.__dni[4:8]

    def CompletaConDatos(self):
        pass

    def CrearCodigoYAsignarCurso(self):
        dic = {'Dto de Artes': 'ING/ART',
            'Dto de Filosofía y Ciencias de la Educación': 'GRA/CEYF',
            'Dto de Física, de Química y Tecnología': 'GRA/FYQ',
            'Dto de Geografia': 'GRA/GEO',
            'Dto de Historia': 'GRA/HIS',
            'Dto de Historia -> Archivistica': 'GRA/ARCH',
            'Dep. de Ingles': 'GRA/INGL',
            'Dto de Matemática': 'ING/MAT',
            'Dto de Letras': 'GRA/LET',
            'Dto de Letras - Teatro': 'GRA/LET',
            'Dto de Música': 'GRA/MUS',
            'Dto de Turismo - Sede Central': 'GRA/TUR',
            'Dto de Turismo - Sede Calingasta': 'GRA/TUR',
            'Dto de Turismo' : 'GRA/TUR',
        }
        if(self.__departamento != 'Otro'):
            self.__departamento = dic[self.__departamento]

    def getNombre(self):
        return (self.__nombre)

    def getApellido(self):
        return (self.__apellido)

    def getEmail(self):
        return (self.__email)

    def getClave(self):
        return (self.__clave)
    
    def getDepartamento(self):
        return(self.__departamento)

    def __eq__(self, other):
        val = False
        conct = self.__apellido + self.__nombre + self.__email + \
            self.__dni + str(self.__numTelefono) + self.__departamento
        conc2 = other.__apellido + other.__nombre + other.__email + \
            other.__dni + str(other.__numTelefono) + other.__departamento

        if (conct == conc2):
            val = True

        return (val)


    def __str__(self):
        return('Nombre: {} - Apellido: {} - DNI: {} \n- Numero de Telefono: {} - Clave {} - Departamento {}'.format(self.__nombre,self.__apellido,self.__dni,self.__numTelefono,self.__clave,self.__departamento))
