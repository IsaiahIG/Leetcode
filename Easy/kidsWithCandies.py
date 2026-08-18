
#8/17/2026
from typing import List
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        
        result = []
        biggest = candies[0]

        for i in candies:
            if i > biggest:
                biggest = i

        for j in range(len(candies)):
            candy = candies[j] + extraCandies

            if candy >= biggest:
                result.append(True)
                print(candy)
            else:
                result.append(False)
                print(candy)
      
        return result 

if __name__  == "__main__":

    solution = Solution()

    candys = [2,3,5,1,3]
    excandys = 3

    result = solution.kidsWithCandies(candys, excandys)

    print (result)