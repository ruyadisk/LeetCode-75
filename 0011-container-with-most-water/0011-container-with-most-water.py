class Solution:
    def maxArea(self, height: List[int]) -> int:
        l = 0
        r = len(height)-1
        maxi = -1
        while(l != r):
            if height[l] > height[r]:
                maxi = height[r] * (r-l) if maxi < height[r] * (r-l) else maxi
                r -= 1
            elif height[l] < height[r]:
                maxi = height[l] * (r-l) if maxi < height[l] * (r-l) else maxi
                l += 1
            else:
                if l+1 != r and l+1 < len(height) and r-1 != l and r-1 > 0:
                    if(height[l+1] > height[r-1]):
                        maxi = height[l] * (r-l) if maxi < height[l] * (r-l) else maxi
                        l += 1
                    else:
                        maxi = height[r] * (r-l) if maxi < height[r] * (r-l) else maxi
                        r -= 1
                else:
                    maxi = height[l] * (r-l) if maxi < height[l] * (r-l) else maxi
                    l += 1
        return maxi