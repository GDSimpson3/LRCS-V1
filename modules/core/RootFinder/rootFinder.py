from modules.base.StationaryPointProcessor.StationaryPointProcessor import StationaryPointProcessor
from modules.base.signChangeScanner.SignChangeScanner import SignChangeScanner
from modules.functional.differentiate.differentiate import Differentiate
from modules.base.findStationaryPoints.findStationaryPoints import FindStationaryPoints
from modules.utils.logger.logger import LOG


def RootFinder(polynomial: list[list[str]],dpAcuraccy:int):


    LOG(f"{'-'*20} ,'FOR POLY', {polynomial}")
    derivative : list[list[str]] = Differentiate(polynomial)

    LOG(f'RECURSIONNNNN --- {derivative} OF - {polynomial}')
    StationaryPoints : list[int] = FindStationaryPoints(derivative,dpAcuraccy)

    LOG(f"STAT POOINTSSS {StationaryPoints} - {derivative}")
    roots :list[int] = []
    StationaryPointRoots, StationaryPointRootPairs = StationaryPointProcessor(polynomial,StationaryPoints)

    LOG(f'ROOT PAIRS --- {StationaryPointRootPairs} ---- {polynomial}')
    for Pair in StationaryPointRootPairs:
        roots.append(SignChangeScanner(Pair[0],Pair[1],polynomial,dpAcuraccy))



    for root in StationaryPointRoots:
        roots.append(root)


    # Edge roots

    # sortedStatPoints = sorted(StationaryPoints)

    # LOG(sortedStatPoints[0])
    # LOG(sortedStatPoints[-1])

    # if sortedStatPoints[0]





    

    return roots