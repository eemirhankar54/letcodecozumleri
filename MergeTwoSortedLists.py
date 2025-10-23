# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
            list3 = ListNode()
            temp = list1
            temp2 = list2
            temp3 = list3
            while temp and temp2:             
                if temp.val < temp2.val:
                    temp3.next = temp
                    temp = temp.next
                else:
                    temp3.next = temp2
                    temp2 = temp2.next

                temp3 = temp3.next

            if temp:
                 temp3.next = temp
            elif temp2:
                 temp3.next = temp2


            return list3.next



#124
#1345
#1,1,2,3,4,4




