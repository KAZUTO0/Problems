class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        if len(nums)==len(set(nums)):
            return False
        else:
            return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna