#1672. Richest Customer Wealth

class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        max_wealth = 0
        for customer in accounts:
            sum_ = sum(account for account in customer)
            max_wealth = max(sum_, max_wealth)
        
        return max_wealth