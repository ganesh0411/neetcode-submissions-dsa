# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head: return False


        temp = head
        hashtable = {}
        hashtable[head] = 1
        while temp.next != None:
            if temp.next in hashtable:
                return True
            else: hashtable[temp.next] = 1

            temp = temp.next
        

        return False
