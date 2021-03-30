class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> count = new HashMap<Integer, Integer>();
        for(int x: nums){
            count.put(x, count.getOrDefault(x, 0) + 1);
        }
        
        Queue<Integer> minHeap = new PriorityQueue<Integer>((a, b) -> Integer.compare(count.get(a), count.get(b)));
        for (int x: count.keySet()){
            if (minHeap.size() == k){
                if (count.get(minHeap.peek()) < count.get(x)){
                    minHeap.remove();                    
                    minHeap.add(x);
                }
            }
            else{
                minHeap.add(x);
            }
        }
        int[] res = new int[k];
        for(int i=0; i< k; i++){
            res[i] = minHeap.remove();
        }
        return res;
    }
}