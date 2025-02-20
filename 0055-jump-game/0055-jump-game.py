class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        pos = [1]
        pos = pos + [0] * (len(nums) - 1) 

        for i in range(len(nums)):
            if pos[i] == 1:
                for j in range(1, nums[i]+1):
                    if i+j < len(pos) - 1:
                        pos[i+j] = 1
                    else:
                        return True
        return False