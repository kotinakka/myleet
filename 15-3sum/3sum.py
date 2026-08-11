class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        res = []
        nums.sort()
        
        # Optimization 3: Only loop up to the third-to-last item
        for i in range(len(nums) - 2):
            
            # Optimization 1: If the lowest number is > 0, the sum can never be 0
            if nums[i] > 0:
                break
                
            # Skip duplicates for the outer loop
            if i > 0 and nums[i] == nums[i-1]:
                continue
            
            l = i + 1
            r = len(nums) - 1
            
            while l < r:
                three_sum = nums[i] + nums[l] + nums[r]
                
                if three_sum < 0:
                    l += 1
                elif three_sum > 0:
                    r -= 1
                else:
                    res.append([nums[i], nums[l], nums[r]])
                    
                    # Optimization 2: Move BOTH pointers inward
                    l += 1
                    r -= 1
                    
                    # Skip duplicates for the left pointer
                    while l < r and nums[l] == nums[l-1]:
                        l += 1
                        
                    # Skip duplicates for the right pointer
                    while l < r and nums[r] == nums[r+1]:
                        r -= 1
                        
        return res

            
        