class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        arr1 = [0] * 26
        arr2 = [0] * 26
        for c in word1:
            arr1[ord(c) - ord('a')] += 1
        for c in word2:
            arr2[ord(c) - ord('a')] += 1

        for i in range(26):
            if (arr1[i] == 0 and arr2[i] != 0) or (arr1[i] != 0 and arr2[i] == 0):
                return False
        arr1 = sorted(arr1)
        arr2 = sorted(arr2)
        print(arr1)
        print(arr2)
        i = 25
        while(i >= 0):
            if arr1[i] != arr2[i]:
                return False
            i -= 1
        return True