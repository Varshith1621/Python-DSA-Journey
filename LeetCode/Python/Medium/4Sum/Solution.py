class Solution(object):
    def fourSum(self, nums, target):
        n = len(nums)
        unique_quads = set()
        
        for i in range(n):
            for j in range(i + 1, n):
                seen = set()
                for k in range(j + 1, n):
                    current_sum = nums[i] + nums[j] + nums[k]
                    fourth = target - current_sum
                    
                    if fourth in seen:
                        # Create a sorted tuple to ensure uniqueness in the set
                        quad = tuple(sorted((nums[i], nums[j], nums[k], fourth)))
                        unique_quads.add(quad)
                        
                    seen.add(nums[k])
                    
        return [list(quad) for quad in unique_quads]