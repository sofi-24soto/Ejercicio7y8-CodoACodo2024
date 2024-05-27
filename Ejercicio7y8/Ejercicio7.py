
#Se crea la clase Cuenta con sus atributos (titular y cantidad)
class Cuenta:
    def __init__(self,titular,cantidad=0):
        self.titular = titular
        self.cantidad = cantidad

    # getters y setters para cada atributo
    def set_titular(self,titular):
        self.titular = titular

    def get_titular(self):     
        return self.titular.nombre , self.titular.edad
    
    def set_cantidad(self,cantidad):
        self.cantidad = cantidad

    def get_cantidad(self):
        return self.cantidad
    
    # Mostrar los datos de la cuenta
    def mostrar(self):
        print("------------- Datos de la Cuenta -------------")
        print("Titular:",self.get_titular()[0])
        print("Cantidad: ${:.3f}".format(self.get_cantidad()))
        print("-----------------------------------------------")

    # Se ingresa la cantidad a la cuenta
    def ingresar(self,cantidad_ingresar):
        print("Cantidad a ingresar: ${:.3f}".format(cantidad_ingresar))
        if cantidad_ingresar > 0:
            self.cantidad += cantidad_ingresar

    # Se retira una cantiddd a la cuenta
    def retirar(self,cantidad_retirar):
       print("Cantidad a retirar:${:.3f}".format(cantidad_retirar))
       if cantidad_retirar > 0:
           self.cantidad -= cantidad_retirar

#Se crea la clase Persona con sus atributos (nombre,edad)
class Persona:
    def __init__(self,nombre,edad):
        self.nombre = nombre
        self.edad = edad
      

     
# Se crea la instancia de la clase Persona   
titular = Persona("Maria López",24)

# Se crea la instancia de la clase Cuenta
cuenta_1 = Cuenta(titular,100.000)

#Mostrar los datos de la cuenta
cuenta_1.mostrar()

#Se ingresa una cantidad a la cuenta
print("---------------- Se ingresa una cantidad ------------")
cuenta_1.ingresar(2.000)
cuenta_1.mostrar()


#Se retira una cantidad a la cuenta
print("---------------- Se retirar una cantidad ------------")
cuenta_1.retirar(1.500)
cuenta_1.mostrar()


