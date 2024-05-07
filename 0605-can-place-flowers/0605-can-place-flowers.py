class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        balance = 0
        n_ = 0
        for cnt in range(len(flowerbed)):
            if flowerbed[cnt] == 0:
                balance -= 1
            if flowerbed[cnt] == 1:
                balance = 1
            if balance == -1 and cnt == len(flowerbed)-1:
                n_ += 1
                balance = 1                
            elif balance == -1 and flowerbed[cnt + 1] != 1:
                n_ += 1
                balance = 1
        return True if n_ >= n else False