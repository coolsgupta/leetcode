def create_linked_list_from_list(ds, ls):
    head = ds()
    head.val = ls[0]
    if len(ls) == 1:
        return head

    head.next = create_linked_list_from_list(ds, ls[1:])
    return head
