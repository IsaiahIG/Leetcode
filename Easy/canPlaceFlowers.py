#8/18/2026
from typing import List

class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:

        

        if flowerbed[0] == 0:
            flowerbed[0] = 1

        for i in range(len(flowerbed)):
            for j in range(i+1,len(flowerbed)):
                if flowerbed[i] == 1 and flowerbed[j] == 1:
                    tf = False
                else:
                    tf = True

        return tf








if __name__ == "__main__":
    solution = Solution()

    lst = [1,0,0,0,1]
    n = 1
    
    result = solution.canPlaceFlowers(lst,n)

    print(result)
