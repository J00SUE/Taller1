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

    #setters

    def verlongitud(self):
        return self.__longitud
    
    def verdiametro(self):
        return self.__diametro
    def vermaterial(self):
        return self.__material

    #getters    

    def asignar_longitud(self,longitud):
        self.__longitud = longitud

    def asignar_diametro(self,diametro):
        self.__diametro = diametro 

    def asignar_material(self, material):
        self.__material = material
        
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

    def verfijacion(self):
        return self.__fijacion
    
    def vertamaño(self):
        return self.__tamaño
    def vermaterial(self):
        return self.__material

    #getters    

    def asignar_fijacion(self,fijacion):
        self.__fijacion = fijacion

    def asignar_tamaño(self,tamaño):
        self.__tamaño = tamaño 

    def asignar_material(self, material):
        self.__material = material
        
class Dentales:
    def __init__(self):
        self.__forma = ""
        self.__fijacion = ""
        self.__material = ""

    #setters

    def verfijacion(self):
        return self.__fijacion
    
    def verforma(self):
        return self.__forma
    def vermaterial(self):
        return self.__material

    #getters    

    def asignar_fijacion(self,fijacion):
        self.__fijacion = fijacion

    def asignar_forma(self,forma):
        self.__forma = forma 

    def asignar_material(self, material):
        self.__material = material

class Sistema:
    def __init__(self):
        self.__dict_paciente = {}
        self.__medico = {}
        self.__dict_cadera = {}
        self.__dict_marca = {}
        self.__dict_coronario = {}
        self.__dict_dentales = {}
        self.__dict_rodilla = {}

    #setters
        
    def verificarExiste(self,cedula):
        for p in self.__dict_paciente:
            if cedula == p.vercedula():
                return True
        #solo luego de haber recorrido todo el ciclo se retorna False
        return False
    
    def verNumeroPacientes(self):
        return len(self.__dict_paciente)
    
     def ingresarPaciente(self, cedula, paciente):
        self.__dict_paciente[cedula] = paciente

    #Delete

    def eliminarPaciente(self, cedula):
        for pac in self.__dict_paciente:
            if cedula == pac.vercedula():
                self.__dict_paciente.pop(pac)  
                return True  #eliminado con exito
        return False
   