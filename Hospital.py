class persona:
    def __init__(self):
        self.nombre = ""
        self.edad = ""
        
class paciente:
    def __init__(self):
        self.eps = ""
        self.operacion = ""

class medico:
    def __init__(self):
        self.especialidad = ""   


class implantes:
    def __init__(self):
        self.implantes = ""

class Cadera:
    def __init__(self):
        self.cadera = " "
        self.material = ""
        self.fijacion = ""
        self.tamaño = 0

    #setters
    #getters

class Marcapasos:
    def __init__(self):
        self.electrodos = 0
        self.alambrico = ""
        self.estimulacion = ""

    #setters
    #getters

class Coronarios:
    def __init__(self):
        self.longitud = 0 
        self.diametro = 0 
        self.material = ""


    #setters
    #getters
        
class Dentales:
    def __init__(self):
        self.forma = ""
        self.fijacion = ""
        self.material = ""

    #setters
    #getters

class Rodilla:
    def __init__(self):
        self.material = ""
        self.fijacion = ""
        self.tamaño = 0

    #setters
    #getters

class Sistema:
    def __init__(self):
        self.paciente = {}
        self.medico = {}
        self.biblio_cadera = {}
        self.biblio_marca = {}
        self.biblio_coronario = {}
        self.biblio_dentales = {}
        self.biblio_rodilla = {}

    #setters
    #getters