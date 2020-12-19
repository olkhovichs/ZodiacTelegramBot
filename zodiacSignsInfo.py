def info_sign():
    infoSigns = {}
    with open("../signsInfo.txt") as file:
        for line in file:
            key, *value = line.split()
            infoSigns[key] = value
    return infoSigns

def dict_to_string(singZodiac):
    descrSign = ''
    descrSign = str(' '.join(allInfoSigns()[singZodiac]))
    return descrSign
