class Solution:
    def jump(self, nums: List[int]) -> int:
        j, cur, far = 0, 0, 0
        for i in range(len(nums) - 1):
            far = max(far, i+nums[i])
            if i == cur:
                j += 1
                cur = far 
        return j