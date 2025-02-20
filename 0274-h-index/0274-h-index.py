class Solution:
    def hIndex(self, citations: List[int]) -> int:
        tbl = [0] * 1001
        for i in citations:
            tbl[i] += 1 
        for j in range(len(tbl)-1, 0, -1):
            if tbl[j] >= j:
                return j
            else:
                tbl[j-1] += tbl[j]
        return 0
                