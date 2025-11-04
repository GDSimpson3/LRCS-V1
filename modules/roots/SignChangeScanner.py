from typing import Union
from modules.computeFX.FX import FX
from modules.error.error import BadInput
from modules.logger.logger import LOG
import time


def SignChangeScanner(StartingPoint:float, EndFlag:float, PolyNomial: list[list[str]], DPAccuracy: int) -> Union[list[float], bool]:
    # TRUE = POSITIVE
    # FALSE = NEGATIVE

    Root = StartingPoint
    End = EndFlag
    Start = Root

    iterationCount = 0
    max_iterations = 1000
    # interval = 2 ** (-1 * iterationCount)
    # direction = (-1) ** (iterationCount)



    while iterationCount < max_iterations:
        def conditionFront(): return Root < End
        def conditionBack(): return Root > End
        def SignCheckFront(): return RootSign() != StartSign()
        def SignCheckBack(): return RootSign() != StartSign() # If either Equal to end, or Not equal to START OF ITERATION RANGE!!!!!!!
        # condition = True # Default Value


        # SignCheck = False # Default Value

        interval = 2 ** (-1 * iterationCount)
        direction = (-1) ** (iterationCount)

        if direction > 0:
            condition = conditionFront
            SignCheck = SignCheckFront
            
        else:
            condition = conditionBack
            SignCheck = SignCheckBack
             
        time.sleep(0.1)
        LOG(f'{Root} --OUT-- {direction} -- COUNT {iterationCount} --- CONDITION = {condition()} --- RAW {condition}')
        
        if not condition():
            time.sleep(0.1)

            LOG(f'FALSE START--------- {Root}  - S {Start} - E {End} - IC {iterationCount}')
            Root = Root + (interval * direction)
            End = Start
            Start = Root
            iterationCount += 1
            LOG(f'FALSE END--------- {Root}  - S {Start} - E {End} - IC {iterationCount}')

        while condition():

            time.sleep(0.1)
            def RootSign(): return FX(PolyNomial,Root) > 0
            def StartSign(): return FX(PolyNomial,Start) > 0
            def EndSign(): return FX(PolyNomial,End) > 0
            
            Root = Root + (interval * direction)
            LOG(f'SIGN CHECK {SignCheck()} ---- {SignCheck}')
            LOG(f'FXXX ---- {Root} --- {FX(PolyNomial,Root)} --- INTERVAL {interval * direction}')
            LOG(f'START ---- {Start} --- {End}')

            if (SignCheck()):
                # Root = Root
                End = Start
                Start = Root
                iterationCount += 1
                LOG(f'SIGN CHECK PASSED: {SignCheck} --- S {Start} --- E {End} --- {Root}')
                time.sleep(0.1)
                break

            if FX(PolyNomial,Root) == 0.0:
                break
            LOG(f'{Root} --- {direction}  ---- {condition()}')
            LOG(f'OUT START ---- {Start} --- {End}')

        if FX(PolyNomial,Root) == 0:
            LOG('YAYAYAYAY')
            break


    return

