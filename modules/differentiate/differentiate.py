

def Differentiate(Polynomial:list[list[str]]) -> list[list[str]]:
    Differentiated : list[list[str]] = []
    for Term in Polynomial:
        Derivative = []

        if Term[1] > 0:
            CoeffiecientDERIVATED = int(Term[0]) * int(Term[1])
            ExponentDERIVATED = Term[1] - 1

            Derivative.append(CoeffiecientDERIVATED)
            Derivative.append(ExponentDERIVATED)
        # else: # Its a constant that should disapear

            Differentiated.append(Derivative)

            
    return Differentiated