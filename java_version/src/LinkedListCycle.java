public class LinkedListCycle {
    public boolean hasCycle(ListNode head) {
        ListNode hare = head;
        ListNode tortoise = head;
        do{
            if(hare==null || tortoise == null || hare.next==null){
                return false;
            }
            hare = hare.next.next;
            tortoise = tortoise.next;
        }while(hare!=tortoise);
        return true;
    }
}
