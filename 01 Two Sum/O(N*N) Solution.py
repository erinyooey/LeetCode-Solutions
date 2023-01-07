class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashmap = {}
        for i in range(len(nums)):
            numTwo = target - nums[i]
            if numTwo in hashmap:
                return [hashmap[numTwo], i]
            else:
                hashmap[nums[i]] = i
