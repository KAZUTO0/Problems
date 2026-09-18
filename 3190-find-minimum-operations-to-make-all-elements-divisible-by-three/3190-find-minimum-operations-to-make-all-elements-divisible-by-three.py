class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        j=0
        for i in nums:
            if i%3!=0:
                j+=1
        return j

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna