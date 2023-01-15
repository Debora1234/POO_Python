#       POO: paradigma muy utilizado
# todos los datos o elemntos que usamos son objetos
# podemos representar y modelar cosas de la vida real.
# obejtos: son elementos o instancias que se crean a partir de una clase
# los obejtos tienen atributos (caraterisitcas) y metodos (funciones)
# caracterisitcas:
#   abstraccion: Define las caracteristicas y funcionalidades de un objeto, osea sus atributos y metodos
#   herencia: Podemos crear un plano de objeto padre y uno plano hijo y relacionarlos, y compartir las caracteristicas y funiones similares
#   polimorfismo: Obejtos que responden de manera diferente ante una misma función
#   encapsulamiento: Evitamos que los objetos se manipulen de manerea incorrecta

#creamos un plano (CLASE) para el objeto PERSONA
#la clase por convención se pone la primera letra en mayuscula y el resto minuscula; y sin espacios

class Persona: 
#con la siguiente linea creamos el constructor de la clase, el constructor sirve para inicializarle 
# los valores a nuestra clase, nombre y edad, son atributos de tipo isntancia, por eso se definen dentro 
# de la clases init
    def __init__(self, nombre, edad):   
        self.nombre=nombre
        self.edad = edad
#atributos, tienen el mismo valor para todos los objetos que se crean a partir de esta clase
    Nacionalidad = "Argentina"
    NumeroDeArea = "+54"
#creamos un metodo de la clase, que sea cumplir años, siempre reciben self, 
#self hace referencia a la instancia de la clase
    def Metodo_Cumpleaños (self):
        self.edad = self.edad + 1
        print("feliz cumpleaños ",self.edad, " ", self.nombre)




#creamos el objeto MARIA, de la clase Persona, osea con el constructor, le tenemos que mandar el nombre y la edad
MARIA = Persona("Maria", 25)
#nos imprime la edad, del objeto MARIA.
print(MARIA.edad)
#nos imprime la altura, del objeto MARIA.
print(MARIA.Nacionalidad)

PACO = Persona("Paco", 32)
PACO.Metodo_Cumpleaños()




#HERENCIA: Creamos una clase a partir de otra clase.
#clase princiapal CLASE PADRE, calse secundaria CLASE HIJO
#se pueden heredar atributos o metodos de la clase principal
class Empleado(Persona):
#tmb podemos crear el contructor de esta clase, pero:
#   si ponemos el constructor asi:
#        def __init__ (self, horas_trabajadas_totales):
#        self.horas_trabajadas_totales = horas_trabajadas_totales
#   solo borramos los parametros de la clase hijo, nombre y edad. 
#   si queremos sumar otro metodo a la clase hijo, dentro del consturcotr debemos hacer lo siguiente
    def __init__ (self, horas_trabajadas_totales, nombre, edad):
        super (Empleado, self).__init__(nombre, edad)
        self.horas_trabajadas_totales = horas_trabajadas_totales
    def Horas_Trabajadas(self, cantidad_horas):
        print("Usted: ", self.nombre, ", ha trabajado: ",cantidad_horas, "horas")


#creamos el primer objeto heredado
ROBERTO=Empleado(2, "Roberto", 25 )
ROBERTO.Horas_Trabajadas(20)
print(ROBERTO.horas_trabajadas_totales)

