class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        ds=0
        ps=0
        for i in str(n):
            ds+=int(i)
            ps+=int(i)**2
        return True if ps-ds>=50 else False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna