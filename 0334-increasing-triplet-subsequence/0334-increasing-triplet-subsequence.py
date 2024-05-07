class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        a = 2**31
        b = 2**31
        for n in nums:
            print(a,b)
            if n <= a:
                a = n
                continue
            elif n <= b:
                b = n
                continue
            else:
                return True
        return False