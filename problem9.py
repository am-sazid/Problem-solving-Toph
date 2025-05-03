def SmartSum(n, coins):
    possible_sums = set()
    possible_sums.add(0)

    for coin in coins:
        new_sums = set()
        for s in possible_sums:
            new_sums.add(s + coin)
        possible_sums.update(new_sums)

    possible_sums.discard(0)  
    result = sorted(possible_sums)
    print(len(result))
    print(" ".join(map(str, result)))

n = int(input())
coins = list(map(int, input().split()))
SmartSum(n, coins)