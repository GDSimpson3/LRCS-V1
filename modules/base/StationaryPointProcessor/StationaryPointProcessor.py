from modules.functional.computeFX.FX import FX
from modules.utils.logger.logger import LOG



#  TRUE == POSITIVE
# FALSE == NEGATIVE

def _Sign(Value:int):
    return Value > 0

def StationaryPointProcessor(Polynomial: list[list[str]], stationaryPoints: list[int]):

    # Check if any stationary points are roots themselves

    SortedStationaryPoints:list[int] = []
    FilteredStationaryPoints:list[int] = []

    StationaryPointRoots : list[int] = []
    StationaryPointRootPairs : list[list[int]] = []

    for Stationarypoint in stationaryPoints:
        # LOG(f'PAIR PROCESSOR -- {Stationarypoint}')
        if FX(Polynomial,Stationarypoint) == 0:
            StationaryPointRoots.append(Stationarypoint)
        else:
            FilteredStationaryPoints.append(Stationarypoint)

    SortedStationaryPoints = sorted(FilteredStationaryPoints)

    LOG(f'PAIR PROCESSOR -- {len(SortedStationaryPoints)}')

    for StatPoint in range(0,len(SortedStationaryPoints) - 1): # -1 because we're gonna compare THIS & the Next, hence the last one will only be in the previous fellas pair
        LOG(f'PAIR PROCESSOR -- {StatPoint}')

        if _Sign(FX(Polynomial,SortedStationaryPoints[StatPoint])) != _Sign(FX(Polynomial,SortedStationaryPoints[StatPoint + 1])):

            Pair = [SortedStationaryPoints[StatPoint], SortedStationaryPoints[StatPoint + 1]]
            StationaryPointRootPairs.append(Pair)

    return StationaryPointRoots, StationaryPointRootPairs
