#ΔTb = i×Kb×m

vantHaffFactor = 2 #NaCl Has 2 ions so 2
massOfSolute = 0 #grams
oneMoleOfSolute = 58.5
massOfSolvent = 0.100 #kg
ebullioscopicConstant = 0.512 #Kb Value of water
normalWaterBoilingTemp = 100
i = 4

def calcTemp():
    moleOfSolute = massOfSolute/oneMoleOfSolute
    molality = moleOfSolute/massOfSolvent
    BoilingPointElevation = vantHaffFactor*ebullioscopicConstant*molality
    return BoilingPointElevation


while i <= 20:
    massOfSolute = i
    BoilingPointElevation = calcTemp()
    print(f"Boiling elevation is: {BoilingPointElevation:.2f}")
    print(f"Boiling Temp is: {BoilingPointElevation + normalWaterBoilingTemp:.2f} for {i} grams of solute")
    i=i+4