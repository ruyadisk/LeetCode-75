class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:    
        
        res = tmp = sum(nums[0:k])
        print(len(nums))
        for i in range(k, len(nums)+1):
            tmp -= nums[i-k] += nums[i]
            res = tmp if tmp > res else res
        return res / k