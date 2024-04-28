def minimum_coins(resto):
    coins = [200, 100, 50, 20, 10, 5, 2, 1]

    min_coins_count = 0
    for coin in coins:
        while resto >= coin:
            resto -= coin
            min_coins_count += 1

    return min_coins_count

resto = int(float(input()) * 100)

print(minimum_coins(resto))