'''
You are given a list of integers representing stock prices for a certain company over a period of time, where each element in the list corresponds to the stock price for a specific day.

You are allowed to buy one share of the stock on one day and sell it on a later day.

Your task is to write a function called max_profit that takes the list of stock prices as input and returns the maximum profit you can make by buying and selling at the right time.

Note that you must buy the stock before selling it, and you are allowed to make only one transaction (buy once and sell once).

Constraints:

Each element of the input list is a positive integer representing the stock price for a specific day.
'''


def max_profit(prices):
    
    minimum = prices[0]
    profit = 0
    for num in prices[1:]:
        current_profit = num - minimum
        profit = max(profit, current_profit)
        minimum = min(minimum, num) 
        
    return profit
    


prices = [7, 1, 5, 3, 6, 4]
profit = max_profit(prices)
print("Test with mixed prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [7, 6, 4, 3, 1]
profit = max_profit(prices)
print("Test with descending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


prices = [1, 2, 3, 4, 5, 6]
profit = max_profit(prices)
print("Test with ascending prices:")
print("Prices:", prices)
print("Maximum profit:", profit)
print("-----------------------------")


"""
    EXPECTED OUTPUT:
    ----------------
    Test with mixed prices:
    Prices: [7, 1, 5, 3, 6, 4]
    Maximum profit: 5
    -----------------------------
    Test with descending prices:
    Prices: [7, 6, 4, 3, 1]
    Maximum profit: 0
    -----------------------------
    Test with ascending prices:
    Prices: [1, 2, 3, 4, 5, 6]
    Maximum profit: 5
    -----------------------------

"""