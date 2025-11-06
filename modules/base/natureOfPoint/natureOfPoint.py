
from modules.functional.computeFX.FX import FX
from modules.functional.differentiate import differentiate


def NatureOfPoint(Derivative:list[list[str]],point:int):

    SecondDerivative = differentiate.Differentiate(Derivative)

    Nature = FX(SecondDerivative,point)

    '''lookin for le gradient changeee'''

    if Nature > 0:
        return 'MIN'
    elif Nature < 0:
        return 'MAX'