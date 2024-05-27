from Ejercicio7 import Cuenta, Persona

class Cuenta_Joven(Cuenta): 
    # Se crea el constructor
    def __init__(self, titular,cantidad=0, bonificacion=0):
        super().__init__(titular, cantidad)
       
        self.bonificacion = bonificacion

    # getters y setters para la bonificacion
    def set_bonificacion(self,bonificacion):
        self.bonificacion = bonificacion
    
    def get_bonificacion(self):
        return self.bonificacion
    
    # Se validad si el titular es mayor  o no
    def es_titular_valido(self):
        edad_titular = self.get_titular()[1]
        return 25 < edad_titular >= 18
    
    # Se retira dinero en caso de que el titular es válido
    def retirar(self, cantidad_retirar):
        if self.es_titular_valido(): 
            super().retirar(cantidad_retirar)
    
    # Se muestra los datos 
    def mostrar(self):

        print("----------- Cuenta Joven -------------")
        print("Bonificación:", self.get_bonificacion())

# Se crea la instancia de la clase Persona
titular_1 = Persona("Pedro Pérez",20)
titular_2 = Persona("Maria López",24)

# Se crea la instancia de la clase Cuenta
cuenta = Cuenta(titular_1,3.000)

# Se crea la instancia de la clase Cuenta joven
cuenta_joven = Cuenta_Joven(titular_2,3.000,10)

cuenta.mostrar()
cuenta_joven.mostrar()











