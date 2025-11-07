import math

from modules.utils.error.error import RootError

def Quadratic(Polynomial: list[list[str]]) -> list[int]:

    a = Polynomial[0][0]
    b = Polynomial[1][0]
    c = Polynomial[2][0]

    Discriminant = (b**2) - (4 * a * c)

    if not Discriminant >= 0:
        RootError(f"Quadratic Root {Polynomial} Has a negative Disciminant - COMPLEX ROOTS")
    
    DiscriminantSQRT = math.sqrt(Discriminant)

    PositiveRoot = ( (-b) + DiscriminantSQRT ) / (2*a)
    NegativeRoot = ( (-b) - DiscriminantSQRT ) / (2*a)

    return PositiveRoot,NegativeRoot



   
    