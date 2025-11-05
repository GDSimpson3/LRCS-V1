def BadInput(msg:str):
    raise ValueError(f'INTERNAL ERROR: {msg}')

def RootError(msg:str):
    raise ValueError(f'INTERNAL ERROR WHILST PROCESSING ROOT: {msg}')




'''
raise ValueError("Bad number")
raise TypeError("Expected a string, got int")
raise RuntimeError("Something went wrong")
raise FileNotFoundError("File not found")
raise KeyError("Missing key in dictionary")
'''