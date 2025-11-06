from modules.functional.computeFX.FX import FX
from modules.utils.error.error import BadInput
from modules.utils.logger.logger import LOG
from modules.utils.sleeper.sleep import SleepFor


def SignChangeScanner(StartingPoint:float, EndFlag:float, PolyNomial: list[list[str]], DPAccuracy: int) -> float:
    # TRUE = POSITIVE
    # FALSE = NEGATIVE

    Root = StartingPoint
    End = EndFlag
    Start = Root

    iterationCount = 0
    max_iterations = 1000
    # interval = 2 ** (-1 * iterationCount)
    # direction = (-1) ** (iterationCount)
    counterrr = 0


    while iterationCount < max_iterations:
        '''
        Keep comparisons as FUNCs so that they're re called every time, AVOID STATIC WRONG COMPARISONNSS

        Additionally re define them each outer while loop
        '''
        counterrr += 1
        
        def conditionFront(): return Root < End
        def conditionBack(): return Root > End
        def SignCheckFront(): return RootSign() != StartSign()
        def SignCheckBack(): return RootSign() != StartSign() # If either Equal to end, or Not equal to START OF ITERATION RANGE!!!!!!!

        # condition = True # Default Value # NO NEED


        # SignCheck = False # Default Value # NO NEED

        interval = 2 ** (-1 * iterationCount)
        direction = (-1) ** (iterationCount)

        if direction > 0:
            condition = conditionFront
            SignCheck = SignCheckFront
            
        else:
            condition = conditionBack
            SignCheck = SignCheckBack
             
        SleepFor(0.1)
        LOG(f'{Root} --OUT-- {direction} -- COUNT {iterationCount} --- CONDITION = {condition()} --- RAW {condition}')
        
        if not condition(): # TO KEEP ITERATING ONCE THE INNER LOOP FALSIFIES, BLYAT THIS KILLED ME
            SleepFor(0.1)

            LOG(f'FALSE START--------- {Root}  - S {Start} - E {End} - IC {iterationCount}')
            Root = Root + (interval * direction)
            End = Start
            Start = Root
            iterationCount += 1
            LOG(f'FALSE END--------- {Root}  - S {Start} - E {End} - IC {iterationCount}')

        while condition():

            SleepFor(0.1)
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
                SleepFor(0.1)
                break

            if FX(PolyNomial,Root) == 0.0:
                break
            LOG(f'{Root} --- {direction}  ---- {condition()}')
            LOG(f'OUT START ---- {Start} --- {End}')

        if round(FX(PolyNomial,Root),DPAccuracy) == 0: # OPTIONAL
            LOG(f'YAYAYAYAY ROOTTT ---- {Root}')
            break


    return round(Root,DPAccuracy)

