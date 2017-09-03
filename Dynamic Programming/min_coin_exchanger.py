def coinchanger(cents, denominations=[1, 5, 10, 20]):
    coins = {d: 0 for d in denominations}
    for c in sorted(coins.keys(), reverse=True):
        coins[c] += cents // c 
        cents = cents % c
        if not cents:
            total_coins = sum([i for i in coins.values()])
            return sorted(coins.items(), reverse=True), total_coins
           
coinchanger(cents=100)
coinchanger(cents=5)
coinchanger(cents=4)
coinchanger(cents=23)
