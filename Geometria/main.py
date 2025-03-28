from punto import Punto
from rectangulo import Rectangulo
import math

if __name__ == "__main__":
    # Puntos
    A = Punto(2, 3)
    B = Punto(5, 5)
    C = Punto(-3, -1)
    D = Punto(0, 0)

    # Imprimir Puntos
    print("Punto A:", A)
    print("Punto B:", B)
    print("Punto C:", C)
    print("Punto D:", D)
    print()

    # Determinar cuadrantes
    print("Cuadrante de A:", Punto.determinar_cuadrante(A))
    print("Cuadrante de C:", Punto.determinar_cuadrante(C))
    print("Cuadrante de D:", Punto.determinar_cuadrante(D))
    print()

    # Calcular vectores
    vector_AB = Punto.calcular_vector(A, B)
    vector_BA = Punto.calcular_vector(B, A)

    print("Vector AB:", vector_AB)
    print("Vector BA:", vector_BA)
    print()

    # Calcular distancias al origen
    print(f"Distancia entre A y B: {Punto.calcular_distancia(A, B):.2f}")
    print(f"Distancia entre B y A: {Punto.calcular_distancia(B, A):.2f}")
    print()

    # Determinar el punto más lejano del origen
    distancias = {
        "A": Punto.calcular_distancia(A, D),
        "B": Punto.calcular_distancia(B, D),
        "C": Punto.calcular_distancia(C, D)
    }

    punto_mas_lejano = max(distancias, key=distancias.get)
    print(f"El punto más lejano del origen es {punto_mas_lejano}")
    print()

    # Crear un rectángulo utilizando los puntos A y B
    rectangulo = Rectangulo(A, B)
    print(f"Punto inicial: {rectangulo.punto_inicial}")
    print(f"Punto final: {rectangulo.punto_final}")
    print(f"Base del rectángulo: {rectangulo.base()}")
    print(f"Altura del rectángulo: {rectangulo.altura()}")
    print(f"Área del rectángulo: {rectangulo.area()}")

    

    
