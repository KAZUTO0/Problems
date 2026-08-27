class Solution:
    def pattern(self, n):
        ans = []

        def helper(x):
            ans.append(x)

            if x <= 0:
                return

            helper(x - 5)
            ans.append(x)

        helper(n)
        return ans

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna