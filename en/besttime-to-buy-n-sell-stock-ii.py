class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        tag = 0
        profit = 0
        for i in range(len(prices)):
            if tag == 0 and self.isbuy(i,prices):
                buy = prices[i]
                tag = 1
            if tag == 1 and self.issell(i,prices):
                profit+=prices[i]-buy
                tag = 0
        return profit

    def isbuy(self,i,prices):
        if i == len(prices)-1:
            return False
        if prices[i]<prices[i+1]:
            return True
        else:
            return False
    def issell(self,i,prices):
        if i==len(prices)-1:
            return True
        elif prices[i]>prices[i+1]:
            return True
        else:
            return False