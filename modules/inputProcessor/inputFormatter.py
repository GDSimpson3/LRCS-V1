import re

from modules.logger.logger import LOG


def _ExtractTermsO(ExtractionStr: str) -> list[str]:
    SEPARATORS = ['+','-']

    Terms: list[str] = []

    # Loop thru ClearRawStr

    Term = "" # Will contain "7X^5"
    SKIPFIRSTChar = False
    for index,character in enumerate(ExtractionStr):

        if index == 0: # Last one, there's no arithmetic operator at the end of the equation, HENCE gotta account for it
            
            # Term = Term + character
            Terms.append(Term)
            SKIPChar = True

        elif character == SEPARATORS[0]:
            # LOG(character)
            Terms.append(Term)
            Term = ""
        elif character == SEPARATORS[1]: # REDO THIS LOGIC LATER
            # LOG(character)
            Terms.append(f"-{Term}")
            Term = ""

        

            # No need to splice ClearRawStr as it's just one loop forwards

        else:
            Term = Term + character
    
    return Terms

def _ExtractTerms(ExtractionStr: str) -> list[str]:
    SEPARATORS = ['+','-']

    Terms: list[str] = []

    # Loop thru ClearRawStr

    Term = "" # Will contain "7X^5"

    ExtractionStrL = ExtractionStr

    if ExtractionStrL[0] != '-':
        ExtractionStrL = '+'+ExtractionStrL

    for index,character in enumerate(ExtractionStrL):
        # LOG(character)
        if index != 0:
            if character == SEPARATORS[0] or character == SEPARATORS[1]:
                Terms.append(Term.replace('+','')) # Remove Plus signs

                Term = ''
        Term = Term + character
        if index == len(ExtractionStrL) -1 :
            Terms.append(Term.replace('+',''))


    # LOG(Terms)
    
    return Terms

def _DecodeTerms(Terms: list[str]) -> list[list[str]]:

    DecodedTerms: list[list[str]] = []

    for Term in Terms:
        SplitedTermRaw = re.split('X',Term)

        # LOG(SplitedTermRaw)
        # LOG(f'++ {Term}')

        Coefficient = SplitedTermRaw[0]
        TermArray = []
        TermArray.append(Coefficient)

        if len(SplitedTermRaw) == 1: # 3 X^1
            TermArray.append(0)
        elif SplitedTermRaw[1] == '': # 3 X^0
            TermArray.append(1)
            # LOG('000')
        else:
            # LOG(int(SplitedTermRaw[1].replace('^','')))
            TermArray.append(int(SplitedTermRaw[1].replace('^','')))
        
        DecodedTerms.append(TermArray)


    
    return DecodedTerms



def InputFormatter(RawStr: str) -> list[list[str]]:

    # 7X^5 - 4X^2 --> ["7X^5","-4X^2"]
    
    # First remove all white spaces

    ClearRawStr = RawStr.replace(" ","")

    ClearRawStr = ClearRawStr.upper()

    # LOG(ClearRawStr)

    ExtractedTerms = _ExtractTerms(ClearRawStr)

    # LOG(ExtractedTerms)

    DecodedArray = _DecodeTerms(ExtractedTerms)

    # LOG(DecodedArray)

    return DecodedArray




        
    
