class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        max_ = gain[0] if 0 < gain[0] else 0
        while(len(gain) > 1):
            gain[1] += gain[0]
            gain = gain[1:]
            max_ = gain[0] if max_ < gain[0] else max_
        return max_