def removeAboveX(x, head):
    temp = head
    while(temp and temp.next):
        if temp.next.val > x:
            temp.next = temp.next.next

        else:
            temp = temp.next

    if head and head.val > x:
        head = head.next

    return head