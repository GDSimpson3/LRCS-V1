


from modules.base.signChangeScanner.SignChangeScanner import SignChangeScanner
from modules.functional.computeFX.FX import FX
from modules.functional.natureOfPoint.natureOfPoint import NatureOfPoint
from modules.utils.logger.logger import LOG


def EndBoundary(Point: int,PolyNomial:list[list[str]]):
    '''
    This is a workaround to Negative infinity

    keep minusing 10 to root till sign change
    '''
    end = Point - 10
    while True:
        if (FX(PolyNomial,end) > 0) != (FX(PolyNomial,Point) > 0):
            return end
        end = end - 100


def EdgeRootScanner(PolyNomial: list[list[str]],SP:float, direction:str,dp:int) -> float:

    Ypos = FX(PolyNomial,SP)
    LOG(Ypos)

    if direction == 'LEFT':
        # Ypos = FX(PolyNomial,SP)

        if Ypos > 0:
            # UP
            if NatureOfPoint(PolyNomial, SP,direction) == 'MAX':
                LOG('GOING UP LEFT MAXXXXXXX')
                root = SignChangeScanner(EndBoundary(SP,PolyNomial),SP,PolyNomial,dp)
                return root
        elif Ypos < 0:
            if NatureOfPoint(PolyNomial,SP, direction) == 'MIN':
                root = SignChangeScanner(EndBoundary(SP,PolyNomial),SP,PolyNomial,dp)
                return root
            # DOWN
        else:
            return # IT IS 0 HENCE TS IS A ROOT ALRRR, it must've alr been considered from the stationary point pairs finder
        

    elif direction == 'RIGHT':

        if Ypos > 0:
            # UP
            if NatureOfPoint(PolyNomial, SP,direction) == 'MAX':
                root = SignChangeScanner(SP,float('inf'),PolyNomial,dp)
                return root
        elif Ypos < 0:
            if NatureOfPoint(PolyNomial,SP, direction) == 'MIN':
                root = SignChangeScanner(SP,float('inf'),PolyNomial,dp)
                return root
            # DOWN
        else:
            return # IT IS 0 HENCE TS IS A ROOT ALRRR, it must've alr been considered from the stationary point pairs finder
        

   

