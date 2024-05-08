class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        arr = [0] * 2001
        res1 = []
        res2 = []
        for _ in nums1:
            if arr[_ + 1000] == 0:
                arr[_+1000] += 1
        for _ in nums2:
            if arr[_ + 1000] == 1:
                arr[_+1000] = -2
            if arr[_ + 1000] == 0:
                arr[_+1000] -= 1
        for _ in range(len(arr)):
            if arr[_] == 1:
                res1.append(_-1000)
            if arr[_] == -1:
                res2.append(_-1000)
        return [res1,res2]