class Solution:
    def missingInteger(self, nums: List[int]) -> int:
        x=nums[0]
        for i,j in pairwise(nums):
            if j==i+1:
                x+=j
            else:
                break
        y=nums
        while x in y:
            x+=1
        return x
                
