class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        l = []
        r = []
        k = k % len(nums)
        for i in range(len(nums)):
            if i < len(nums)-k:
                r.append(nums[i])
            else:
                l.append(nums[i])
        res = l + r
        for i in range(len(nums)):
            nums[i] = res[i]
        
        