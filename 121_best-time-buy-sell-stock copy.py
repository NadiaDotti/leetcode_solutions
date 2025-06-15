import timeit

class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        sum = 0
        min_price = prices[0]
        for price in prices[1:]:
            if price < min_price:
                min_price = price
            elif price - min_price > sum:
                sum = price - min_price
        return sum
    
    
if __name__ == "__main__":
    sol = Solution()
    prices = [1, 2, 3, 4, 5]
    
    def call():
        output = sol.maxProfit(prices)
        print("Output:", output)
    tempo = timeit.timeit(call, number=1)
    print(f"Tempo impiegato: {tempo:.6f} secondi")
    