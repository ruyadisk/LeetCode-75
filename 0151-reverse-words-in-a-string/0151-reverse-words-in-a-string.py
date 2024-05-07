class Solution:
    def reverseWords(self, s: str) -> str:
        x = s.split(' ')
        res = ""
        print(x)
        for i in range(len(x)-1, -1, -1):
            if x[i] != " " and x[i] != "":
                print(x[i])
                res+=x[i]
                res+=" "
        return res[:-1]