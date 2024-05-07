import math
class Solution:
    def compress(self, chars: List[str]) -> int:
        res = 0
        i = 0
        while(i < len(chars)):
            pre = chars[i]
            count = 0
            while(i < len(chars) and chars[i] == pre):
                count += 1
                i += 1
            chars[res] = pre
            res += 1
            if count > 1:
                for _ in str(count):
                    chars[res] = _
                    res += 1
        return res

            