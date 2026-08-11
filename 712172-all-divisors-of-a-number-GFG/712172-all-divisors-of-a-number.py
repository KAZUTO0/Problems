class Solution:
    def getDivisors(self, n):
        x=[]
        for i in range(1,int(n**(0.5))+1):
            if n%i==0:
                x.append(i)
                if i!=(n//i):
                    x.append(n//i)
        return sorted(x)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna