def WelcomeMessage():

    WelcomeMessageString = '''Welcome to LRCS-V1
    
    This tool will allow you to find the roots of any polynomial

    Though there are some exceptions:
    - The function CANNOT have assymptotes
    - The function Cannot Flat line
    - NO complex roots please

    To see/turn Off Logs, go to config.py and set ENV to 'DEV'

    Runtime: python 3.13.2

    Write in this form:

        1X^4 -2X^3 -5X^2 + 6X
        coefficientX^exponent

    And with That, A теперь наслаждайтесь!
'''
    print('-' * 6)
    print(WelcomeMessageString)
    print('-' * 6)

    return