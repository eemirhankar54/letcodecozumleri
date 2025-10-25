class Solution(object):
    def lengthOfLastWord(self, s):
        
        sayac = 0

        s = s.strip()

        for i in range(len(s) - 1, -1 ,-1):
            if s[i] == " ":
                break
            sayac += 1

        return sayac 
           

        
                
       #hello world     