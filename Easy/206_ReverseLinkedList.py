# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# def checkNode(n, curr):
#     if n is None:
#         return
#     if n.next:
#         curr = checkNode(n.next, curr)
#     curr.next = ListNode(n.val)
#     return curr.next
#
# def reverseList(head):
#     curr = new_head = ListNode()
#     checkNode(head, curr)
#     return new_head.next

def reverseList(head):
    prev = None
    curr = head
    while curr:
        c_next = curr.next
        curr.next = prev
        prev, curr = curr, c_next
    return prev


print(reverseList(ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))))
