class Solution(object):
    def addBinary(self, a, b):
        c = ""
        if len(a) < len(b):
            a = a.zfill(len(b))
        else:
            b = b.zfill(len(a))

        elde = 0

        for i in range(len(a)-1,-1,-1):
            toplam = int(a[i]) + int(b[i]) + elde
            if toplam == 2:
                c += "0"
                elde = 1
            elif toplam == 3:
                c += "1"
                elde = 1
            else :
                c += str(toplam)
                elde = 0
            
        if elde == 1:
            c += "1"

        return c[::-1]