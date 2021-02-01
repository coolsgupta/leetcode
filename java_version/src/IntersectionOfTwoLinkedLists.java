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
