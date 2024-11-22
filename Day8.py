#Stock Buy and Sell – Max one Transaction Allowed

def maxProfit(prices):
    # Edge case: If there's only one price or no price, no transaction is possible
    if not prices or len(prices) == 1:
        return 0
    
    # Initialize variables
    min_price = float('inf')  # Initially, set min_price to infinity
    max_profit = 0  # Initialize the maximum profit as 0
    
    # Iterate through the prices array
    for price in prices:
        # Update the min_price to the lowest price seen so far
        if price < min_price:
            min_price = price
        # Calculate the potential profit if sold today
        profit = price - min_price
        # Update max_profit if the current profit is greater than the previous max
        if profit > max_profit:
            max_profit = profit
    
    return max_profit
