class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = ['a','e','i','o','u','A','E','I','O','U']
        d = []
        a = "123"
        print(a[1])
        for cnt in range(len(s)):
            if s[cnt] in vowels:
                d.append(cnt)
        print(d)
        while(len(d) >= 2):
            s = s[0:d[0]] + s[d[-1]] + s[(d[0]+1):d[-1]] + s[d[0]] + s[(d[-1]+1):]
            d = d[1:-1]
        return s
            