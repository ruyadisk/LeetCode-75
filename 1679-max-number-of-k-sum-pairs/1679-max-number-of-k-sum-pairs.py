class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        res = 0
        l = 0
        r = 0
        while(r < len(nums) and nums[r] < k):
            r+=1
        if r == 0:
            return 0
        else:
            nums = nums[0:r]
            r = r-1
            while(l < r):
                if nums[l] + nums[r] == k:
                    res += 1
                    l += 1
                    r -= 1
                elif nums[l] + nums[r] < k:
                    l += 1
                else:
                    r -= 1
        return res