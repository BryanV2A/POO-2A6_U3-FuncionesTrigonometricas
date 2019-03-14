"""
>>> fT = funcionesTrigonometricas(10)
>>> fT.calcularSeno()
0.17364817766693033
>>> fT.calcularCoseno()
0.984807753012208
>>> fT.calcularTangente()
0.17632698070846498
"""

"""
Para hacer las pruebas unitarias primero se tiene que agregar entre comentarios (Triples comillas) los tres mayor que (>>>) al inicio y sin identacion y
después declarar el nombre del objeto y el nombre y de la clase, después agregar el método al que va a acceder el objeto
y abajo lo que se espera obtener.
"""

import math
"""
Se importa la librería math para poder realizar las operaciones de seno, coseno y tangente.
"""
class funcionesTrigonometricas:

    """
    Datos necesitados para poder realizar la operacion
    """
    __numG = float(0)
    __numG2 = float(0)
    __resultadoSeno = float(0)
    __resultadoCoseno = float(0)
    __resultadoTangente = float(0)

    def __init__(self, numG):
        self.__numG = numG
        self.__numG2 = math.radians(self.__numG)

    """
    Dentro del método constructor se realiza la conversion del valor float a radianes para realizar las respectivas 
    operaciones.
    """

    """
    Se declara el método constructor con un solo valor a ingresar, que es el ángulo que introducirá el usuario.
    """

    def calcularSeno(self):
        self.__resultadoSeno = math.sin(self.__numG2)
        return self.__resultadoSeno

    """
    Método donde se calcula el Seno del ángulo ingresado
    """

    def calcularCoseno(self):
        self.__resultadoCoseno = math.cos(self.__numG2)
        return self.__resultadoCoseno

    """
    Método donde se calcula el Coseno del ángulo ingresado
    """


    def calcularTangente(self):
        self.__resultadoTangente = math.tan(self.__numG2)
        return self.__resultadoTangente

    """
    Método donde se calcula el Tangente del ángulo ingresado
    """

if __name__==  '__main__':
    import doctest
    doctest.testmod()
"""
Sintaxis correspondientes a la prueba unitaria
"""