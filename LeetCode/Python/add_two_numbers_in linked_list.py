# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l3=[]
        i=0
        for i in range(len(l1)):
            l3.append(l1[i]+l2[i])
            i=i+1
            print(f"i is {i} , l3[i] is {l3[i-1]}")
        return l3