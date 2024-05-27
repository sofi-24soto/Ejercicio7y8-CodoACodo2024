# Ejercicio7y8-CodoACodo2024

## Índice
* [1. Ejercicio 7](#1-ejercicio-7)
* [2. Ejercicio 8](#2-ejercicio-8)
* [3. Tecnología Utilizada](#4-tecnologia-utilizada)
* [4. Personas Contribuyente](#4-personas-contribuyentes)

***
## 1. Ejercicio 7
    Crea una clase llamada Cuenta que tendrá los siguientes atributos: titular (que es una
persona) y cantidad (puede tener decimales). El titular será obligatorio y la cantidad es
opcional. Crear los siguientes métodos para la clase:
  * Un constructor, donde los datos pueden estar vacíos.
  * Los setters y getters para cada uno de los atributos. El atributo no se puede modificar
directamente, sólo ingresando o retirando dinero.
  * Mostrar(): Muestra los datos de la cuenta.
  * Ingresar(cantidad): se ingresa una cantidad a la cuenta, si la cantidad introducida es
negativa, no se hará nada.
  * Retirar(cantidad): se retira una cantidad a la cuenta. La cuenta puede estar en números
rojos.

***

## 2. Ejercicio 8
   Vamos a definir ahora una “Cuenta Joven”, para ello vamos a crear una nueva clase
CuantaJoven que deriva de la clase creada en el punto 7. Cuando se crea esta nueva clase,
además del titular y la cantidad se debe guardar una bonificación que estará expresada en
tanto por ciento. Crear los siguientes métodos para la clase:
 * Un constructor.
 * Los setters y getters para el nuevo atributo.
 * En esta ocasión los titulares de este tipo de cuenta tienen que ser mayor de edad, por lo
tanto hay que crear un método es_titular_valido() que devuelve verdadero si el titular es
mayor de edad pero menor de 25 años y falso en caso contrario.
 * Además, la retirada de dinero sólo se podrá hacer si el titular es válido.
 * El método mostrar() debe devolver el mensaje de “Cuenta Joven” y la bonificación de la
cuenta.

***
## 3. Tecnología Utilizada
   * Python
***
## 4. Personas Contribuyentes
   * Sofia A. Soto | Front-End | Argentina  