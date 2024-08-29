class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high+1)//2 - (low//2)   
    #(high + 1) // 2 gives the number of odd numbers from 1 to high
    #low // 2 gives the number of odd numbers from 1 to low - 1