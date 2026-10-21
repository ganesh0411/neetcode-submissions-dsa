# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def find_mid(self, head):
        slow = head
        fast = head.next

        while fast and fast.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow

    def split_list(self, mid):
        temp = mid.next
        mid.next = None
        head2 = temp
        return head2
    
    def reverse_list (self, head):
        previous = None
        current_node = head

        while current_node:
            temporary_node = current_node.next
            current_node.next = previous
            previous = current_node
            current_node = temporary_node

        return previous

    def zip_merge_lists(self, list1, list2):
        dummy_node = ListNode(0, list1)
        l1 = list1
        l2 = list2

        while l1 and l2:
            temporary_node = l1.next
            l1.next = l2
            l1 = temporary_node
            temporary_node = l2.next
            l2.next = l1
            l2 = temporary_node

        return dummy_node.next


    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = self.find_mid(head)
        head_list2 = self.split_list(mid)
        reversed_head2 = self.reverse_list(head_list2)
        merged_list = self.zip_merge_lists(head, reversed_head2)

