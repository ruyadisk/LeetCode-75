class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        l = 0
        r = 0
        while(l < len(s)):
            while(r < len(t)):
                if l == len(s):
                    break
                if t[r] != s[l]:
                    r+=1
                else:
                    l+=1
                    r+=1
            if l != len(s):        
                return False
        return True