class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n==1:
            return True
        if n<=0 or n%2!=0:
            return False
        return self.isPowerOfTwo(n//2)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna