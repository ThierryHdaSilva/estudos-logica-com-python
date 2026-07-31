import math


def calcular_area_circulo(raio):
    """Calcula a área de um círculo a partir do raio."""
    if raio < 0:
        raise ValueError("O raio não pode ser negativo.")
    return math.pi * raio**2


def calcular_area_triangulo(base, altura):
    """Calcula a área de um triângulo."""
    if base < 0 or altura < 0:
        raise ValueError("Base e altura não podem ser negativas.")
    return (base * altura) / 2


def calcular_area_retangulo(largura, altura):
    """Calcula a área de um retângulo."""
    if largura < 0 or altura < 0:
        raise ValueError("Largura e altura não podem ser negativas.")
    return largura * altura
