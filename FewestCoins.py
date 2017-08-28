def recMC(coinValueList, change):
    minCoins = change
    if change in coinValueList:
        return 1
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recMC(coinValueList, change-i)
            if numCoins < minCoins:
                minCoins = numCoins
    return numCoins

def recDC(coinValueList, change, knownResults):
    minCoins = change
    if change in coinValueList:
        knownResults[change] = 1
        return 1
    elif knownResults[change] > 0:
        return knownResults[change]
    else:
        for i in [c for c in coinValueList if c <= change]:
            numCoins = 1 + recDC(coinValueList, change-i,
                                 knownResults)
            if numCoins < minCoins:
                minCoins = numCoins
                knownResults[change] = minCoins
    return minCoins

def dpMakeChange(coinValueList, change, minCoins, coinsUsed):
    """从0开始，直到我们要求的零钱，依次计算需要的硬币数，填入字典中，以便之后的循环使用"""
    for cents in range(change+1):
        coinCount = cents
        newCoin = 1
        for j in [c for c in coinValueList if c <= cents]:
            if minCoins[cents-j] + 1 < coinCount:
                coinCount = minCoins[cents-j] + 1
                newCoin = j
        minCoins[cents] = coinCount
        coinsUsed[cents] = newCoin
    return minCoins[change]

def printCoins(coinsUsed, change):
    coin = change
    while coin > 0:
        thisCoin = coinsUsed[coin]
        print(thisCoin)
        coin = coin - thisCoin

if __name__ == '__main__':
    amnt = 63
    clist = [1, 5, 10, 21, 25]
    coinsUsed = [0] * (amnt+1)
    coinCount = [0] * (amnt+1)

    print('Making change for', amnt, 'requires')
    print(dpMakeChange(clist, amnt, coinCount, coinsUsed), 'coins')
    print('They are:')
    printCoins(coinsUsed, amnt)
    print('The used list is as follows:')
    print(coinsUsed)