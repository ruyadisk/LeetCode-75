class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        l = 0
        r = len(nums) - 1
        if r == -1:
            return 0
        if r == 0:
            return 0 if nums[0] == val else 1
        while(l <= r):
            if nums[l] != val:
                l += 1
            elif nums[r] == val:
                r -= 1
            else:
                nums[l] = nums[r]
                nums[r] = val
        return l
        
        