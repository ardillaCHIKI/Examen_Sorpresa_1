class Punto:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __str__(self):
        return f"({self.x},{self.y})"
    
    def determinar_cuadrante(punto):
        if punto.x > 0 and punto.y > 0:
            return "Primer cuadrante"
        elif punto.x < 0 and punto.y > 0:
            return "Segundo cuadrante"
        elif punto.x < 0 and punto.y < 0:
            return "Tercer cuadrante"
        elif punto.x > 0 and punto.y < 0:
            return "Cuarto cuadrante"
        elif punto.x == 0 and punto.y != 0:
            return "Eje Y"
        elif punto.y == 0 and punto.x != 0:
            return "Eje X"
        else:
            return "Origen"
        
    def calcular_vector(punto1, punto2):
        return (punto2.x - punto1.x, punto2.y - punto1.y)
    