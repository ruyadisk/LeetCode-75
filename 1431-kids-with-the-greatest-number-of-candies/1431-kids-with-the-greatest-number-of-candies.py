class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        res = []
        m = max(candies)
        for k in candies:
            if k + extraCandies < m:
                res.append(False)
            else:
                res.append(True)
        return res