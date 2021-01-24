# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        list_map = []
        print(lists)
        for i, x in enumerate(lists):
            if not x:
                continue

            heapq.heappush(list_map, (x.val, i))

        heapq.heapify(list_map)

        res = None

        print(list_map)
        while (True):
            if not list_map:
                break

            min_val = heapq.heappop(list_map)
            if min_val is None:
                break

            temp = ListNode(min_val[0])
            if lists[min_val[1]].next:
                lists[min_val[1]] = lists[min_val[1]].next
                heapq.heappush(list_map, (lists[min_val[1]].val, min_val[1]))

            if not res:
                res = temp
                a = res

            else:
                a.next = temp
                a = a.next

        return res

