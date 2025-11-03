from typing import Union
from modules.computeFX.FX import FX
from modules.error.error import BadInput
from modules.logger.logger import LOG



def SignChangeScanner(StartingPoint:float, EndFlag:float, PolyNomial: list[list[str]], DPAccuracy: int) -> Union[list[float], bool]:
    # TRUE = POSITIVE
    # FALSE = NEGATIVE

    Root = StartingPoint
    End = EndFlag
    Start = Root

    iterationCount = 0
    
    # interval = 2 ** (-1 * iterationCount)
    # direction = (-1) ** (iterationCount)



    while True:
        def conditionFront(): return Root < End
        def conditionBack(): return Root > End
        def SignCheckFront(): return RootSign != StartSign 
        def SignCheckBack(): return RootSign != EndSign
        condition = True # Default Value


        SignCheck = False # Default Value

        interval = 2 ** (-1 * iterationCount)
        direction = (-1) ** (iterationCount)

        if direction > 0:
            condition = conditionFront
            SignCheck = SignCheckFront
            
        else:
            condition = conditionBack
            SignCheck = SignCheckBack
             

        LOG(f'{Root} --OUT-- {direction}')
        
        while condition():
            RootSign = Root > 0
            StartSign = Start > 0
            EndSign = End > 0
            
            Root = Root + (interval * direction)


            if (SignCheck()):
                # Root = Root
                End = Start
                Start = Root
                iterationCount += 1
                break

            # if FX(PolyNomial,Root) == 0.0:
            #     break
            LOG(f'{Root} --- {direction}')

        # if FX(PolyNomial,Root) == 0:
        #     LOG('YAYAYAYAY')


    return