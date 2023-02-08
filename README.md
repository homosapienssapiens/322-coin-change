# 322-coin-change
The [challenge No. 322](https://leetcode.com/problems/coin-change/) in leetcode.com

## Overview
This challenge was made by using the grid method. The code uses an array that has the length of the amount give plus one.

## Solution process
This challenge needs to go through a set of coins and obtain the lowest quantity of coins possible for the exact amount and if the amount can´t be made by any combination, it is needed to return -1.

The following code (found in the .py file of this repository) is the solution I created for this problem by using grid method.


```python
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
```

## Challenge description
You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.
Return the fewest number of coins that you need to make up that amount. If that amount of money cannot be made up by any combination of the coins, return -1.
You may assume that you have an infinite number of each kind of coin.
