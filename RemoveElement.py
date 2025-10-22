class Solution(object):
    def removeElement(nums, val):
        sayac = 0
        for i in range(len(nums)-1,-1,-1):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                sayac += 1
            
        return sayac