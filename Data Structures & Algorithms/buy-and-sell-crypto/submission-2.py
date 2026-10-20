class Solution:
    def maxProfit(self, price: List[int]) -> int:
        # l,r = 0,1
        # maxP = 0
        # while r< len(price):
        #     if price[l] < price[r]:
        #         profit = price[r]-price[l]
        #         maxP = max(maxP, profit)
        #     else:
        #         l = r
        #     r+=1
        # return maxP
        maxP = 0
        minBuy = price[0]

        for sell in price:
            maxP = max(maxP, sell - minBuy)
            minBuy = min(minBuy, sell)
        return maxP