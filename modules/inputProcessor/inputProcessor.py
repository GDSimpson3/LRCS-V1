from config import ENVIRONMENT
from modules.inputProcessor.inputFormatter import InputFormatter


def InputProcessorMain(Message) -> list[list[str]]:
    RawStrInput = str(input(Message))

    if ENVIRONMENT == 'DEV':
        RawStrInput = '7X^6 + 4X^2 - 8X^3 + 3x + 3'
        # RawStrInput = '8x^3 -40x^2 + 46x -15'
    return InputFormatter(RawStrInput)

 