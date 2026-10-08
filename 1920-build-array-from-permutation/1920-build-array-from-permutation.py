class Solution:
    def buildArray(self, nums: list[int]) -> list[int]:
        a=[]
        def f(n):
            if n<0:
                return
            a.append(nums[nums[n]])
            return f(n-1)
        f(len(nums)-1)
        i=[*reversed(a)]
        return i

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna