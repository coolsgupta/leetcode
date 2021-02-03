public class MeetingRoomsII {
    public int minMeetingRooms(int[][] intervals) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>();

        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        for(int[] x: intervals){
            if (heap.size()==0){
                heap.add(x[1]);
            }
            else{
                if(heap.peek() <= x[0]){
                    heap.remove();
                }
                heap.add(x[1]);
            }
        }
        return heap.size();
    }
}
