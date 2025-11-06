
from modules.functional.computeFX.FX import FX
from modules.functional.differentiate.differentiate import Differentiate


def NatureOfPoint(PolyNomial:list[list[str]],point:int, direction:str):

    Derivative = Differentiate(PolyNomial)
    SecondDerivative = Differentiate(Derivative)

    Nature = FX(SecondDerivative,point)

    '''lookin for le gradient changeee'''

    if Nature > 0:
        return 'MIN'
    elif Nature < 0:
        return 'MAX'
    else:
        # return 'INFL'

        '''INFLECTION POINT LOGIC
        
        SIMPLY LOOKS AT INFINTE SIDE TO SEE IF ITS GOING UP OR DOWN TO CALL IT A MIN / MAX

        PDF SLIDE 12 SHOWS THIS
        '''

        if direction == 'LEFT':
            if FX(PolyNomial,point) > 0: # UP
                if FX(PolyNomial,point - 100) < FX(PolyNomial,point): # Going Down
                    return 'MAX'
            elif FX(PolyNomial,point) < 0: # DOWN
                if FX(PolyNomial,point - 100) > FX(PolyNomial,point): # Going UP
                    return 'MIN'
        elif direction == 'RIGHT':
            if FX(PolyNomial,point) > 0: # UP
                if FX(PolyNomial, point + 100) > FX(PolyNomial,point): # Going Down
                    return 'MAX'
            elif FX(PolyNomial,point) < 0: # DOWN
                if FX(PolyNomial,point + 100) < FX(PolyNomial,point): # Going UP
                    return 'MIN' 