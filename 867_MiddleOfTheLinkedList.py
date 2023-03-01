# naive:
def middleNode(head):
    curr = head
    l = 0
    while curr.next is not None:
        l += 1
        curr = curr.next
    for i in range(0, l / 2 if l % 2 == 0 else l / 2 + 1, 1):
        head = head.next
    return head

# cool:
def middleNode_cool(head):
    slow = head
    fast = head.next
    while fast:
        slow = slow.next
        if fast.next:
            fast = fast.next.next
        else:
            fast = None
    return slow
