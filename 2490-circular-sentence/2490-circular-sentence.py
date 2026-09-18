class Solution:
    def isCircularSentence(self, sentence: str) -> bool:
        x = sentence.split(" ")
        for i in range(len(x)):
            if x[i-1][-1] != x[i][0]:
                return False
        return True

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna