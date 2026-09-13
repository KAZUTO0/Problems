class Solution:
    def countFriendsPairings(self, n: int) -> int:
        if n<=2:
            return n
       
        return self.countFriendsPairings(n-1) + ((n-1) * self.countFriendsPairings(n-2))
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna