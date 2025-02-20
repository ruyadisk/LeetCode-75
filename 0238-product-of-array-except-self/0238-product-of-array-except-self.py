class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ans = [1] * len(nums)
        
        pre = 1
        for i in range(len(nums)-1):
            pre *= nums[i]
            ans[i+1] *= pre
        post = 1
        for j in range(len(nums)-1, 0, -1):
            post *= nums[j]
            ans[j-1] *= post
        
        return ans


        