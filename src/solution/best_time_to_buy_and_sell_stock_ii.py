from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        buy_price = float("inf")

        for price in prices:
            if price < buy_price:
                buy_price = price
                continue

            if price > buy_price:
                profit += price - buy_price
                buy_price = price

        return profit
