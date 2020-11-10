def allInfoSigns():
    infoSigns = {}
    with open("/Users/semenolhovic/Python_Projects/telegram/signsInfo.txt") as file:
        for line in file:
            key, *value = line.split()
            infoSigns[key] = value
    return infoSigns

def dictToString(singZodiac):
    descrSign = ''
    descrSign = str(' '.join(allInfoSigns()[singZodiac]))
    return descrSign
