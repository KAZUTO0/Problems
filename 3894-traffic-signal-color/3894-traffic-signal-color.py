class Solution:
    def trafficSignal(self, timer: int) -> str:
        # timer=int(input())
        if timer==0:
            return 'Green'
        elif timer==30:
            return 'Orange'
        elif timer in range(31,91):
            return 'Red'
        else:
            return 'Invalid'

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna