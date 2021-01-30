public class ReverseLinkedList {
    public ListNode reverseList(ListNode head) {
        if (head!=null){
            ListNode temp = head.next;
            head.next = null;
            while(temp!=null){
                ListNode temp2 = temp.next;
                temp.next = head;
                head = temp;
                temp = temp2;
            }
        }
        return head;
    }
}
