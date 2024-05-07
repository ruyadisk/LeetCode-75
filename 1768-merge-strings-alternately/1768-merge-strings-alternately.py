class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        res = ""
        (flg, n) = (False, len(word1)) if len(word1) < len(word2) else (True, len(word2))
        while(n>0):
            res+=word1[0]
            res+=word2[0]
            word1 = word1[1:]
            word2 = word2[1:]
            n-=1
        if flg == True:
            res += word1
        else:
            res += word2
        return res