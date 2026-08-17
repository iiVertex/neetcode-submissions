class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i,x in enumerate(nums):
            for j,y in enumerate(nums):
                if i == j:
                    break
                if x + y == target:
                    return [j,i]