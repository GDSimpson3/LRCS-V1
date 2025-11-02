from typing import Union
from modules.computeFX.FX import FX
from modules.error.error import BadInput
from modules.logger.logger import LOG

import numpy as np


def SignChangeScanner(StartingPoint:float, EndFlag:float, PolyNomial: list[list[str]], DPAccuracy: int) -> Union[list[float], bool]:
    # TRUE = POSITIVE
    # FALSE = NEGATIVE

    Start = StartingPoint
    End = EndFlag

    StartSign = FX(PolyNomial,Start) > 0
    EndSign = FX(PolyNomial,End) > 0

    IterationCount = 0

    Interval = 2 ** (-1 * IterationCount)
    Direction = (-1) ** IterationCount

    

    if StartSign == EndSign:
        BadInput("Both Starting and end values have the same Sign")
        return
    
    # Root = 
    while True:
        # for Root in range(Start,End,Interval * Direction):
        for Root in np.arange(Start, End, Interval * Direction):
            LOG(f'((((())))) {Root}')
            RootSign = FX(PolyNomial,Root) > 0

            if (RootSign != StartSign):
                LOG(f'{RootSign != StartSign} ==== {Root}')

                End = Start
                Start = Root
                IterationCount += 1

            if FX(PolyNomial,Root) == 0:
                LOG(f'___ {Root}')
                return False
                # break
   




