# Best Time to Buy and Sell Stock (LeetCode 121)

prices = [7, 1, 5, 3, 6, 4]

buy_price = float("inf")
profit = 0


for current_price in prices:
    if current_price < buy_price:
        buy_price = current_price
    elif current_price - buy_price > profit:
        profit = current_price - buy_price

print(profit)

