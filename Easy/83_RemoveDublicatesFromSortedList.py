def deleteDuplicates(head):
    if head is None:
        return head
    prev, curr = head, head.next
    while curr:
        if prev.val == curr.val:
            prev.next = curr.next
        else:
            prev = curr
        curr = curr.next
    return head
