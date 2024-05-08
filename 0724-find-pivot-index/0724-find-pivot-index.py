class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        l = 0
        r = sum(nums)
        for _ in range(len(nums)):
            r -= nums[_]
            if r == l:
                return _
            l += nums[_]
        return -1