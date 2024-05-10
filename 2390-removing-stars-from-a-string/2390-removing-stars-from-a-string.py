class Solution:
    def removeStars(self, s: str) -> str:
        stack = []
        for c in s:
            if c != "*":
                stack.append(c)
            else:
                stack.pop()
        res = ""
        for c in stack:
            res += c
        return res