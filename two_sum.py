class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        if len(nums) > 1:
            target_pair = dict()
            
            for i in range(len(nums)):
                
                diff = target - nums[i]
                
                if nums[i] in target_pair:
                    return[i, target_pair[nums[i]]]
                else:
                    target_pair[diff] = i
                
