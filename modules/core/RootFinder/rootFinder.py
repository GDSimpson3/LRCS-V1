from modules.functional.differentiate.differentiate import Differentiate
from modules.base.findStationaryPoints.findStationaryPoints import FindStationaryPoints


def RootFinder(polynomial: list[list[str]]):
    derivative = Differentiate(polynomial)
    StationaryPoints = FindStationaryPoints(derivative)

    

    return 'sdfs'