# -*- coding: utf-8 -*-
"""
Created on Wed Feb  8 10:43:09 2023

@author: Consultant
"""

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        arr = [float('inf')] * (amount + 1)
        arr[0] = 0
        for i in range(1, amount + 1):
            for coin in coins:
                if i >= coin:
                    arr[i] = min(arr[i], arr[i - coin] + 1)
        return arr[amount] if arr[amount] != float('inf') else -1