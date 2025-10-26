class Solution(object):
    def plusOne(self, digits):


        digits2 = list(digits)
        elde = 1

        for i in range(len(digits2)-1,-1,-1):
            if elde == 0:
                break

            yeni_deger = digits2[i] + elde

            if yeni_deger == 10:
                digits2[i] = 0
                elde = 1
            else:
                digits2[i] = yeni_deger
                elde = 0

            
        if elde == 1:
            digits2.insert(0,1)
                
            
        return digits2