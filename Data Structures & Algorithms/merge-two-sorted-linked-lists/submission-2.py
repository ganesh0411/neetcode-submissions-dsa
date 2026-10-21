# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode, list2: ListNode) -> ListNode:
        placeholder_head = ListNode()
        last_merged = placeholder_head

        while list1 and list2:
            if list1.val < list2.val:
                last_merged.next = list1
                list1 = list1.next
            else:
                last_merged.next = list2
                list2 = list2.next
            last_merged = last_merged.next

        last_merged.next = list1 or list2

        return placeholder_head.next
















