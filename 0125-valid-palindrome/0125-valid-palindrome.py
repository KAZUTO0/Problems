import re
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=re.sub(r"[^a-z0-9]", "", s)
        left=0
        right=len(s)-1
        x=True
        while left<right:
            if s[left]!=s[right]:
                x=False
                break
            else:
                x=True
            left+=1
            right-=1
        return x

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna