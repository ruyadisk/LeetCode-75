class Solution:
    def __init__(self):
        self.vowel = ['a','e','i','o','u']
        self.res = 0
    def maxVowels(self, s: str, k: int) -> int:
        for _ in range(0, k):
            if s[_] in self.vowel:
                self.res += 1
        self.cnt = self.res
        for _ in range(k, len(s)):
            print(s[_-k+1], s[_], self.cnt, self.res)
            if s[_-k+1] not in self.vowel:
                    if s[_] in self.vowel:
                        self.cnt += 1
                        self.res = self.cnt if self.cnt > self.res else self.res
            if s[_-k+1] in self.vowel:
                if k == 1:
                    return 1
                if s[_] not in self.vowel:
                    self.cnt  = self.cnt - 1 if self.cnt > 0 else 0 
        return self.res