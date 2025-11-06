from modules.utils.error.error import RootError


def Linear(polynomial: list[list[str]]):
    degree = polynomial[0][0]

    if degree != 1:
        RootError("WRONG POLYNOMIAL PASSED")
    
    # [['1','1'],['-3.4343','0']]

    root = (-1 * polynomial[1][0]) / polynomial[0][0]

    return root
