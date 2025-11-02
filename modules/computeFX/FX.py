def FX(Polynomial: list[list[str]], X) -> float:
    FXSum = 0

    for Term in Polynomial:
        FXSum = float(FXSum) + float((float(Term[0]) * (X ** float(Term[1]))))
    
    
    return FXSum