from typing import Union
from modules.computeFX.FX import FX


def SignChangeScanner(StartingPoint:int, EndFlag:int, PolyNomial: list[list[str]], DPAccuracy: int) -> Union[list[float], bool]:

    base = 2
    exponent = 0
    interval = base ** exponent # Keep changing intervals in powers of 2, start with 2^0

    StartingPointVar = StartingPoint
    EndingPointVar = EndFlag
    # TRUE == POSITIVE, FALSE == NEGATIVE
    StartingSign = FX(PolyNomial,StartingPoint) > 0 # Initialising, if yes then true, else false
    Direction = 1

    while True:
        for PotentialRoot in range(StartingPointVar,EndingPointVar, (interval * Direction)): # Go from Start to End in interval, interval is change for direction, - going back, + goin front
            # FX(PolyNomial,Position) 
            PotentialRootSign = FX(PolyNomial,PotentialRoot) > 0

            if (PotentialRootSign != StartingSign): # Initialising value compared against Current value




    return