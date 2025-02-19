class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        tar = int(len(nums)/2) + 1
        tbl = {}
        for i in nums:
            if f'{i}' in tbl:
                tbl[f'{i}'] += 1
            else:
                tbl[f'{i}'] = 1
            if tbl[f'{i}'] >= tar:
                return i
