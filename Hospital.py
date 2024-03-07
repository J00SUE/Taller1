class persona:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0 
        self.__edad = ""
        self.__genero = ""
        
class paciente:
    def __init__(self):
        self.__eps = ""
        self.__operacion = ""

class medico:
    def __init__(self):
        self.__especialidad = ""   


class implantes:
    def __init__(self):
        self.__implantes = ""

class Cadera:
    def __init__(self):
        self.__cadera = " "
        self.__material = ""
        self.__fijacion = ""
        self.__tamaño = 0

    #setters
    #getters

class Marcapasos:
    def __init__(self):
        self.__electrodos = 0
        self.__alambrico = ""
        self.__estimulacion = ""

    #setters
    #getters

class Coronarios:
    def __init__(self):
        self.__longitud = 0 
        self.__diametro = 0 
        self.__material = ""


    #setters
    #getters
        
class Dentales:
    def __init__(self):
        self.__forma = ""
        self.__fijacion = ""
        self.__material = ""

    #setters
    #getters

class Rodilla:
    def __init__(self):
        self.__material = ""
        self.__fijacion = ""
        self.__tamaño = 0

    #setters
    #getters

class Sistema:
    def __init__(self):
        self.__paciente = {}
        self.__medico = {}
        self.__biblio_cadera = {}
        self.__biblio_marca = {}
        self.__biblio_coronario = {}
        self.__biblio_dentales = {}
        self.__biblio_rodilla = {}

    #setters
    #getters