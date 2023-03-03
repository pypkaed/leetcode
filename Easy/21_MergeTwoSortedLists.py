# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def mergeTwoLists(list1, list2):
    head = res = ListNode()
    while list1 and list2:
        if list1.val < list2.val:
            res.next = list1
            list1 = list1.next
        else:
            res.next = list2
            list2 = list2.next
        res = res.next

    while list1 or list2:
        res.next = list1 if list1 else list2
        res = res.next
        list1 = list1.next if list1 else None
        list2 = list2.next if list2 else None

    return head.next


list1 = ListNode(1, ListNode(2, ListNode(4)))
list2 = ListNode(1, ListNode(3, ListNode(4)))
print(mergeTwoLists(list1, list2))
