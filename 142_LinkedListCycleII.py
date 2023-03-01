def detectCycle(head):
    slow = fast = head
    while fast and fast.next:
        slow, fast = slow.next, fast.next.next
        if slow == fast:
            break
    else:
        return
    while head != slow:
        head, slow = head.next, slow.next
    return slow
