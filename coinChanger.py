# Return a list representing a coin system
# that contains coins from pennies up to
# one hunder dollar bills
# NOTE: All of your coins/bills 
# should be of the data type float
# Benjamin Gutierrez
def init_StdSystem():
    '''
    >>> init_StdSystem()
    [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    '''
    return [100.0, 50.0, 20.0, 10.0, 5.0, 1.0, .5, .25, .1, .05, .01]

# Write a function that makes a 
# list containing all of the standard 
# coins up to the inputted max coin value.
# If max_val is none, return the standard system.
# Benjamin Gutierrez
def init_CoinSystem(max_val):
    '''
    >>> init_CoinSystem(5)
    [5.0, 1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    >>> init_CoinSystem(1)
    [1.0, 0.5, 0.25, 0.1, 0.05, 0.01]
    >>> init_CoinSystem(-1)
    'error'
    '''
    if max_val is None:
        return init_StdSystem()
    if max_val < 0:
        return "error"
    coinList = init_StdSystem()
    length = len(coinList)
    index = -1
    max_val = float(max_val)
    for i in range(0,length):
        if coinList[i] == max_val:
            index = i
    resultList = coinList[index:]
    return resultList



# Write a function that takes in a coin system
# and creates a dictionary that contains 
# each coin as a key with each coin having
# an associated value of 0.  
# Benjamin Gutierrez
def init_ChangeDict(coin_system):
    '''
    >>> C = init_CoinSystem(1)
    >>> init_ChangeDict(C)
    {1.0: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    >>> S = init_StdSystem()
    >>> init_ChangeDict(S)
    {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 0, 1.0: 0, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0}
    '''
    dictCoin = {}
    for i in coin_system:
        dictCoin.update({i:0})
    return dictCoin
# Check if it is possible to give 
# exact change with the given coin system
# For simplicity's sake, you should just
# check that the money is at least greater than
# the smallest available coin. 
# Benjamin Gutierrez
def isValidChange(money, coin_system):
    '''
    >>> S = init_StdSystem()
    >>> isValidChange(.001, S)
    False
    >>> isValidChange(.15, S)
    True
    '''
    if coin_system[len(coin_system)-1] > money:
        return True
    else:
        return False
    

# If coin change cannot be made, return an error message. 
# Return a tuple in the form (min_coins, coin_dict)
# where min_coins is the minimum number of coins required
# and coin_dict is a dictionary that returns how many
# of each coin was used. 
# Benjamin Gutierrez
def coinChange(money, max_coin_val=None):
    '''
    >>> coinChange(1)
    (1, {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 0, 1.0: 1, 0.5: 0, 0.25: 0, 0.1: 0, 0.05: 0, 0.01: 0})
    >>> coinChange(5.75)
    (3, {100.0: 0, 50.0: 0, 20.0: 0, 10.0: 0, 5.0: 1, 1.0: 0, 0.5: 1, 0.25: 1, 0.1: 0, 0.05: 0, 0.01: 0})
    '''
    num_coins = 0
    coinSystem = init_CoinSystem(max_coin_val)
    if isValidChange(money, coinSystem) == False:
        return "error"
    coinDict = init_ChangeDict(coinSystem)
    for i in coinDict:
        while money - i > 0:
            num_coins = num_coins + 1
            coinDict.update({i: coinDict.get(i)+1})
    return (num_coins, coinDict)
