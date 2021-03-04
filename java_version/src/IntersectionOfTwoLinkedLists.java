public class IntersectionOfTwoLinkedLists {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        Set<ListNode> a = new HashSet<ListNode>();
        while(headA!=null){
            a.add(headA);
            headA = headA.next;
        }
        while(headB!=null){
            if (a.contains(headB))
                break;
            headB = headB.next;
        }
        return headB;
    }
}

// optimized for O(1) space
public class Solution {
    public ListNode getIntersectionNode(ListNode headA, ListNode headB) {
        ListNode pa = headA;
        ListNode pb = headB;

        while(pa != pb){
            pa = pa == null? headB: pa.next;
            pb = pb == null? headA: pb.next;
        }

        return pa;

    }
}