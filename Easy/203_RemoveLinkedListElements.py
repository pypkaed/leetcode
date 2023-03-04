def removeElements(head, val):
    prev = None
    curr = head
    while curr:
        if curr.val == val:
            if prev:
                prev.next = curr.next
            else:
                head = curr.next
        else:
            prev = curr
        curr = curr.next
    return head
