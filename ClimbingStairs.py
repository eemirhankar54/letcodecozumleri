class Solution(object):
    def climbStairs(self, n):
        f = [1,2]

        for i  in range(2,n):
            f.append(f[i-1] + f[i-2])
            if  i == n:
                break
        
        return f[n-1]
            