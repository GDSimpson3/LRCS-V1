from modules.functional.QuadraticCompute.Quadratic import Quadratic
from modules.functional.linearCompute.linear import Linear


def FindStationaryPoints(derivative:list[list[str]], dpAccuracy:int):
    degree = derivative[0][1]

    stationaryPoints: list[int] = []

    if degree == 2:
        PosRt, NegRt = Quadratic(derivative)
        stationaryPoints.append(PosRt)
        stationaryPoints.append(NegRt)

    elif degree == 1:
        Linroot = Linear(derivative)
        stationaryPoints.append(Linroot)
    
    else:
        from modules.core.RootFinder.rootFinder import RootFinder # Lazy import, only taken when needed

        Roots = RootFinder(derivative,dpAccuracy)

        stationaryPoints = Roots


    
    return stationaryPoints