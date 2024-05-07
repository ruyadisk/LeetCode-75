class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod = 1
        cache = 1
        firstlock = False
        doublelock = False

        res = []
        for n in nums:
            if n == 0 and firstlock == False:
                firstlock = True
            elif n == 0 and firstlock == True and doublelock == False:
                doublelock = True
            else:
                prod = prod * n
        if(doublelock == True):
            return [0] * len(nums)
        for n in nums:
            if firstlock == True and n != 0:
                res.append(0)
            elif n == 0:
                res.append(prod)
            else:
                res.append(int(prod / n))
        return res

