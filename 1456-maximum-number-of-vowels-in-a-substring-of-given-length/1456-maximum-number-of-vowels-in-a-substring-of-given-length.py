class Solution:
    def __init__(self):
        self.vowel = ['a','e','i','o','u']
        self.res = 0
        self.cnt = 0
    def maxVowels(self, s: str, k: int) -> int:
        if k == 1:
            for c in s:
                if c in self.vowel:
                    return 1
        for _ in range(0, k):
            if s[_] in self.vowel:
                self.res += 1
        self.cnt = self.res
        for _ in range(k, len(s)):
            if s[_-k] not in self.vowel and s[_] in self.vowel:
                self.cnt += 1
                self.res = self.cnt if self.cnt > self.res else self.res
            elif s[_-k] in self.vowel and s[_] not in self.vowel:
                self.cnt  = self.cnt - 1 if self.cnt > 0 else 0
        return self.res