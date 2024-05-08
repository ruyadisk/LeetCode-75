class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = 0
        while(len(gain) > 0):
            max_ = gain[0] if max_ < gain[0] else max_
            gain[1] += gain[0]
            gain = gain[1:]
        return max_