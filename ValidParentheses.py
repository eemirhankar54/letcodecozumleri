class Solution(object):
    def isValid(self, s):
        stack = []

        eslesme = {')' : '(' , ']' : '[' , '}':'{'}

        for karakter in s:
            if karakter in '([{':
                stack.append(karakter)
            else:
                if not stack or stack[-1] != eslesme[karakter]:
                    return False
                stack.pop()
        
        return not stack

        

