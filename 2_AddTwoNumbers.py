class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def addTwoNumbers(l1, l2):
    res = ListNode()
    cur = res
    carry = 0

    while l1 or l2 or carry:
        val1 = l1.val if l1 else 0
        val2 = l2.val if l2 else 0

        val = val1 + val2 + carry
        carry = val // 10
        val %= 10
        cur.next = ListNode(val)

        cur = cur.next
        l1 = l1.next if l1 else None
        l2 = l2.next if l2 else None

    return res.next


one = ListNode(2, ListNode(4, ListNode(3)))
two = ListNode(5, ListNode(6, ListNode(4)))
print(addTwoNumbers(one, two))
