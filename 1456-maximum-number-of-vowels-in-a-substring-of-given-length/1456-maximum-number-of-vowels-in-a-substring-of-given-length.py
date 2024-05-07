class Solution:
    def __init__(self):
        vowel = ['a','e','i','o','u']
        res = 0
        cnt = 0
    def maxVowels(self, s: str, k: int) -> int:
        vowel = ['a','e','i','o','u']
        res = 0
        cnt = 0
        for _ in range(0, k):
            if s[_] in vowel:
                res += 1
        cnt = res
        for _ in range(k, len(s)):
            if s[_-k] not in vowel and s[_] in vowel:
                cnt += 1
                res = cnt if cnt > res else res
            elif s[_-k] in vowel and s[_] not in vowel:
                cnt = cnt - 1 if cnt > 0 else 0
        return res