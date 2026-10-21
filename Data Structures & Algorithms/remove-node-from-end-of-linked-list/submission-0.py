# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:

    def length(self, head):
        if head is None:
            return 0 

        count = 1
        traversal_node = head
        while traversal_node and traversal_node.next is not None:
            traversal_node = traversal_node.next
            count += 1
        return count

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        position_from_beginning = self.length(head) - n + 1
        node_count = 1
        slow = dummy = ListNode()
        dummy.next = head
        fast = head

        while fast:
            if node_count == position_from_beginning:
                slow.next = fast.next
                break
            node_count+= 1
            slow = slow.next
            fast = fast.next
        return dummy.next


