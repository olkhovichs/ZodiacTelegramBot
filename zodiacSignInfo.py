def inf():
    d = {}
    with open("/Users/semenolhovic/Python_Projects/telegram/signsInfo.txt") as file:
        for line in file:
            key, *value = line.split()
            d[key] = value
    return d
