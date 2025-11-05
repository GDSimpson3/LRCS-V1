<h1 align='center'>Locating roots VIA Change in Sign - LRCS-V1</h1>

## Overall Flow

This program aims to locate the roots of a polynomial up to any degree. It works as so:
1) Locate stationary points of polynomial VIA Differentiation and recursion
2) Scan through if any of the stationary points are roots themselves (this is to filter out roots that touch the X axis, processing them through the oscillation algorithm would break it as detecting a sign change would be impossible)
3) Take the first leftmost stationary point And judge whether there's a root beyond in the negative direction (if its a minimum and above the X axis, that means that there isn't a root beyond, similarly if its a max and below the X axis)
4) Look at pairs of stationary points and see if there's a sign change between them, if so, there's a root residing in between em.
5) Once a root is detected, we pass it into the **SignChangeScanner** module, This module will go from the first stationary point to the next, once it detects the sign change, it will go backwards in much smaller intervals. it will carry on like this till the root is located to a certain degree of acuraccy
6) It will conduct the SignChangeScanner for all detected roots and return them all in an array


<h1 align='center'>MODULES</h1>

## Input Processing

**Input format**: `7X^6 + 4X^2 - 8X^3 + 3x + 3`

**I**: `Polynomial: string`

**O** `Polynomial: List[List[str]]`

### Input cleansing

Make all the X's Capital and Eradicate all blank spaces VIA Regex

### Decoding: 

Split through the Operators `['+','-']` into an array
 
`7X^6 + 4X^2 - 8X^3 + 3x + 3` --> `["7X^6", "4X^2", "-8X^3", "3x", "3"]`

Take each term, and split it into coefficient and exponent to leave the computed form

`["7X^6", "4X^2", "-8X^3", "3x", "3"]` --> `[["7","6"], ["4","2"], ["-8","3"], ["3","1"], ["3","0"]]`

Note: Special cases for exponents of 1 and 0

## Computing FX

I: `Polynomial: List[List[str]]`, `X: Int`

O: `FX: Int`

### Procedure

Loop through each term and sum the multiplication of the coefficient with X raised to the terms exponent

## Derivative Calculation

I: `Polynomial: List[List[str]]`

O: `Polynomial: List[List[str]]`

It simply conducts a Power rule differentiation with each term. Constants are eriadicated and non existent terms aren't considered

## SignChangeScanner

I: `StartingPoint:float, EndFlag:float, PolyNomial: list[list[str]], DPAccuracy: int`

O: `Union[list[float], bool]`

There were some technical difficulties with this a python's default Range does not support increment by floats. Hence a custom double While loop was implemented.

Conditions were dynamic and switched in ascending powers of `(-1)` to change direction everytime the root was passed. Increments were `2^(-incrementCount)`, this allowed increments to become smaller and smaller and acurately reach the root

## Stationary Point Processor

I: `Polynomial: list[list[str]], stationaryPoints: list[int]`

O: `StationaryPointRoots: list[list[int]]`

It takes in an array of stationary points that are sorted in ascending order. It first checks if any points themselves are roots, those startionary points are considered seperately. Next it loops through the array and it compares each point with the one in front. If a sign change (of FX) is detected, there's a root between them and it's saved.

## Logger [UTIL]

Custom Logging module, Clears all logs when environment is set to Prod (`ENVIRONMENT != 'DEV'`)

## Custom Error Handler [UTIL]

Custom Error handling module

## Custom Time Sleeper [UTIL]

Custom Time handling module, Dissables in Prod (`ENVIRONMENT != 'DEV'`)

<h1 align='right'>Credits</h1>
I got a few gray hairs thanks to this.... this honestly was much more twisty than I thought it would be. You had to be IN the state for it. You couldn't just clear your mind and come back.. no no no нетттт. It was like starting from scratch.....

But I'd be lying if I said that this wasn't enjoyable.

Collaborators: @gdsimpson3, @gdsimpson3 and @gdsimpson3