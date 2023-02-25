def maxProfit(prices):
    max_diff = 0
    min_price = prices[0]
    for i in range(0, len(prices)):
        min_price = min(min_price, prices[i])
        max_diff = max(max_diff, prices[i] - min_price)

    return max_diff


def maxProfit_bad(prices):
    max_diff = 0
    for i in range(0, len(prices) - 1):
        for j in range(i + 1, len(prices)):
            if prices[j] - prices[i] > max_diff:
                max_diff = prices[j] - prices[i]
    return max_diff


print(maxProfit([2, 4, 1]))
print(maxProfit([7, 1, 5, 3, 6, 4]))
print(maxProfit([7, 6, 4, 3, 1]))
print(maxProfit([3, 2, 6, 5, 0, 3]))
print(maxProfit([1, 2]))
print()
print(maxProfit_bad([2, 4, 1]))
print(maxProfit_bad([7, 1, 5, 3, 6, 4]))
print(maxProfit_bad([7, 6, 4, 3, 1]))
print(maxProfit_bad([3, 2, 6, 5, 0, 3]))
print(maxProfit_bad([1, 2]))
