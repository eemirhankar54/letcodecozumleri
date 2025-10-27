class Solution(object):
    def twoSum(self, nums, target):
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                aranan_sayi = target - nums[i]
                if aranan_sayi == nums[j]:
                    return i,j
