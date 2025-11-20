class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)

        for i in range(n):
            for j in range(i+1,n):
                if nums[i]+nums[j] == target:
                    return [i,j]

class Solution2:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        seen = {} #heatmap(dict)

        for i , num in enumerate(nums):
            difference = target - num

            if difference in seen:
                return [seen[difference], i]

        seen[num] = i
