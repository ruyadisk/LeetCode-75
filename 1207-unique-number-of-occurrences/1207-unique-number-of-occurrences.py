class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        occ = [0] * 1000
        pos = 0
        cnt = 0
        tmp = -1001
        for i in arr:
            if i != tmp:
                if occ[cnt] != 0:
                    return False
                else:
                    occ[cnt] = i
                    pos += 1
                    cnt = 1
                    tmp = i
            else:
                cnt += 1
        if cnt == len(arr):
            return True
        if occ[cnt] != 0:
            return False
        else:
            return True