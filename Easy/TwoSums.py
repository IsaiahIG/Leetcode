#8/15/2026
from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = []
        
        if len(nums) < 0:
            return 0
        
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] + nums[j] == target:
                    arr.append(i)
                    arr.append(j)
    
        return arr

if __name__ == "__main__":

    solution = Solution()

    myarr = [3,2,3]
    target = 6


    result = solution.twoSum(myarr,target)

    print(result)