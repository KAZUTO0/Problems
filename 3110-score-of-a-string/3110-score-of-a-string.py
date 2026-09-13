class Solution:
    def scoreOfString(self, s: str) -> int:
        def f(i):
            if i==len(s)-1:
                return 0
            x=abs(ord(s[i])-ord(s[i+1]))
            return x+f(i+1)
        return f(0)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna