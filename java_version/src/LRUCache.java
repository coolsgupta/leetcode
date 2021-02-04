class DLLNode{
    public int key;
    public int value;
    public DLLNode next;
    public DLLNode prev;

    public DLLNode(int k, int v){
        this.key = k;
        this.value = v;
        this.next = null;
        this.prev = null;
    }
}

class LRUCache {
    public DLLNode head;
    public DLLNode tail;
    public Map<Integer, DLLNode> cache;
    public int size;
    public int n;

    public LRUCache(int capacity) {
        this.n = capacity;
        this.size = 0;
        this.head = new DLLNode(0, 0);
        this.tail = new DLLNode(0, 0);
        this.cache = new HashMap<Integer, DLLNode>();

        this.head.next = this.tail;
        this.tail.prev = this.head;
    }

    public void addNode(DLLNode node){
        node.next = this.head.next;
        node.prev = this.head;
        this.head.next.prev = node;
        this.head.next = node;
    }

    public void delNode(DLLNode node){
        node.prev.next = node.next;
        node.next.prev = node.prev;
    }

    public DLLNode pop(){
        DLLNode node = this.tail.prev;
        this.delNode(node);
        return node;
    }

    public void reorder(DLLNode node){
        this.delNode(node);
        this.addNode(node);
    }

    public int get(int key) {
        if (!this.cache.containsKey(key))
            return -1;

        DLLNode node = this.cache.get(key);
        this.reorder(node);
        return node.value;

    }

    public void put(int key, int value) {
        if (!this.cache.containsKey(key)){
            if (this.size < this.n){
                this.size++;
            }
            else{
                DLLNode node = this.pop();
                this.cache.remove(node.key);
            }
            DLLNode node = new DLLNode(key, value);
            this.addNode(node);
            this.cache.put(key, node);
        }
        else{
            DLLNode node = this.cache.get(key);
            node.value = value;
            this.reorder(node);
        }
    }
}

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */