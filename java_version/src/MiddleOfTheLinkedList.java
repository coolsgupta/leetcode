public class MiddleOfTheLinkedList {
    public ListNode middleNode(ListNode head) {
        ListNode mid = head;
        while(head!=null){
            head = head.next;
            if (head != null){
                head = head.next;
                mid = mid.next;
            }
        }
        return mid;
    }
}
