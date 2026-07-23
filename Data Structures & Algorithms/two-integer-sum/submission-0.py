class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d={}
        for i in range(len(nums)):
            num=nums[i]
            compli=target-num
            if compli in d:
                return [d[compli],i]
            d[num]=i