class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        l = 0
        r = 1
        dic = []
        if len(nums) == 1:
            return 1
        while(r < len(nums)):
            print(l,r)
            if nums[r] == nums[l]:
                if r == len(nums)-1:
                    if r - l >= 1:
                        dic.append((nums[r],True))
                    else:
                        dic.append((nums[r],False))
                    break
                r += 1
            else:
                if r - l > 1:
                    dic.append((nums[l], True))
                else:
                    dic.append((nums[l], False))
                l = r
        cnt = 0
        for x, y in dic:
            if y:
                nums[cnt] = x
                nums[cnt+1] = x
                cnt += 2
            else:
                nums[cnt] = x
                cnt += 1
        return cnt