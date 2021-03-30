class MedianFinder {

    /** initialize your data structure here. */
    PriorityQueue<Integer> minHeap;
    PriorityQueue<Integer> maxHeap;
    int total;
    public MedianFinder() {
        this.minHeap = new PriorityQueue<Integer>();
        this.maxHeap = new PriorityQueue<Integer>(Collections.reverseOrder());
        this.total = 0;
    }
    
    public void addToMinHeap(int num){
        if (this.maxHeap.peek() <= num){
            this.minHeap.add(num);
        }
        else{
            this.minHeap.add(this.maxHeap.remove());
            this.maxHeap.add(num);            
        }
    }
    
    public void addToMaxHeap(int num){
        if (this.minHeap.peek() >= num){
                this.maxHeap.add(num);
        }
        else{
            this.maxHeap.add(this.minHeap.remove());
            this.minHeap.add(num);
        }
    }
    
    public void addNum(int num) {
        if (this.total == 0){
            this.maxHeap.add(num);
        }
        else if (this.total == 1){
            this.addToMinHeap(num);
        }
        else if (this.total %2 == 0){
            this.addToMaxHeap(num);
        }
        else{
            this.addToMinHeap(num);
        }
        this.total++;
    }
    
    public double findMedian() {
        if (this.total%2 == 1){
            return this.maxHeap.peek();
        }
        else{
            return Double.valueOf(this.minHeap.peek() + this.maxHeap.peek())/2;
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */