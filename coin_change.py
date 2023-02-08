# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:43:09 2023

@author: Consultant
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
    # Initialize an array with float('inf') values, except for the first element which is set to 0
    arr = [float('inf')] * (amount + 1)
    arr[0] = 0

    # Loop through the possible amounts from 1 to amount
    for i in range(1, amount + 1):
        # Loop through each coin
        for coin in coins:
            # If the current amount is greater than or equal to the coin value
            if i >= coin:
                # Update the minimum number of coins needed to make the current amount
                arr[i] = min(arr[i], arr[i - coin] + 1)

    # Return the minimum number of coins needed to make amount
    # If arr[amount] is still equal to float('inf'), it means there's no solution and we return -1
    return arr[amount] if arr[amount] != float('inf') else -1
