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
                    # diff = target - nums[i]
                    # we are trying to find if a number diff exists as nums[j]
                    # so we can return [i,j]. For now lets just store i while we look for j
                    target_pair[diff] = i
                
