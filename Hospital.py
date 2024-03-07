class persona:
    def __init__(self):
        self.__nombre = ""
        self.__cedula = 0 
        self.__edad = ""
        self.__genero = ""

        #getters

    def vernombre(self):
        return self.__nombre 
    
    def vercedula(self):
        return self.__cedula
    
    def veredad(self):
        return self.__edad
    
    def vergenero(self):
        return self.__genero
    
        #Setters

    def asignar_nombre(self,nombre):
        self.__nombre = nombre

    def asignar_cedula(self,cedula):
        self.__cedula = cedula
    
    def asignar_edad(self,edad):
        self.__edad = edad

    def asignar_genero(self,genero):
        self.__genero = genero


        
class paciente:
    def __init__(self):
        self.__eps = ""
        self.__operacion = ""

    #setters
        
    def vereps(self):
        return self.__eps
    
    def verop(self):
        return self.__operacion
    
    #getters

    def asignar_eps(self,eps):
        self.__eps = eps 
    
    def asignar_op(self,op):
        self.asignarop = op

class medico:
    def __init__(self):
        self.__especialidad = ""  

        #setters 

    def verespe(self):
        return self.__especialidad


        #getters

    def asignar_espe(self,espe):
        self.__especialidad = espe


class implantes:
    def __init__(self):
        self.__implantes = ""

        #setters 

    def verimplantes(self):
        return self.__implantes


        #getters

    def asignar_implantes(self,implantes):
        self.__implantes = implantes
    

class Cadera:
    def __init__(self):
        self.__cadera = " "
        self.__material = ""
        self.__fijacion = ""
        self.__tamaño = 0

    #setters

    def vermaterial(self):
        return self.__material
    
    def verfijacion(self):
        return self.__fijacion
    
    def vertamaño(self):
        return self.__tamaño

    #getters    

    def asignar_material(self,material):
        self.__material = material

    def asignar_fijacion(self,fijacion):
        self.__fijacion = fijacion 

    def asignar_tamaño(self,tamaño):
        self.__tamaño = tamaño
    

class Marcapasos:
    def __init__(self):
        self.__electrodos = 0
        self.__alambrico = ""
        self.__estimulacion = ""

    #setters

    def verelectrodos(self):
        return self.__electrodos
    
    def veralambrico(self):
        return self.__alambrico
    def verestimulacion(self):
        return self.__estimulacion

    #getters    

    def asignar_electrodos(self,electrodos):
        self.__electrodos = electrodos

    def asignar_alambrico(self,alambrico):
        self.__alambrico = alambrico 

    def asignar_estimulacion(self,estimulacion):
        self.__estimulacion = estimulacion

class Coronarios:
    def __init__(self):
        self.__longitud = 0 
        self.__diametro = 0 
        self.__material = ""

    
        
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