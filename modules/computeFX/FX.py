def FX(Polynomial: list[list[str]], X) -> int:
    FXSum = 0

    for Term in Polynomial:
        FXSum = FXSum + (Term[0] * (X ** Term[1]))
    
    
    return FXSum