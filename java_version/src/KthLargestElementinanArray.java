public class KthLargestElementinanArray {
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(Collections.reverseOrder());
        for (int x: nums)
            heap.add(x);

        for(int i=0; i<k-1; i++)
            heap.remove();

        return heap.remove();

    }

    // using heap of only size k
    public int findKthLargest(int[] nums, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();
        for (int x: nums){
            if(k>0){
                heap.add(x);
                k--;
            }
            else{
                if (x > heap.peek()){
                    heap.remove();
                    heap.add(x);
                }
            }
        }
        return heap.remove();
    }

}
