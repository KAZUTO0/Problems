class Solution:
    def validDigit(self, n: int, x: int) -> bool:
        s = str(n)
        return s[0] != str(x) and str(x) in s

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna