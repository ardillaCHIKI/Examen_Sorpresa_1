import math

class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def determinar_cuadrante(punto):
        if punto.x > 0 and punto.y > 0:
            return "Esta en el primer cuadrante"
        elif punto.x < 0 and punto.y > 0:
            return "Esta en el segundo cuadrante"
        elif punto.x < 0 and punto.y < 0:
            return "Esta en el tercer cuadrante"
        elif punto.x > 0 and punto.y < 0:
            return "Esta en el cuarto cuadrante"
        elif punto.x == 0 and punto.y != 0:
            return "Esta en el Eje Y"
        elif punto.y == 0 and punto.x != 0:
            return "Esta en el Eje X"
        else:
            return "Esta en el origen"
        
    def calcular_vector(punto1, punto2):
        return (punto2.x - punto1.x, punto2.y - punto1.y)
    
    def calcular_distancia(punto1, punto2):
        return math.sqrt((punto2.x - punto1.x)**2 + (punto2.y - punto1.y)**2)
    