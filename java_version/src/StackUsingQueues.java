class MyStack {
    /** Initialize your data structure here. */
    Queue<Integer> queue;
    int top;
    boolean flag;

    public MyStack() {
        this.queue = new LinkedList<Integer>();
    }

    /** Push element x onto stack. */
    public void push(int x) {
        this.queue.add(x);
        this.top = x;
        this.flag = true;
    }

    /** Removes the element on top of the stack and returns that element. */
    public int pop() {
        Queue<Integer> temp = new LinkedList<Integer>();
        int top = this.queue.remove();

        while(!this.queue.isEmpty()){
            temp.add(top);
            top = this.queue.remove();
        }
        this.queue = temp;
        this.flag = false;
        return top;

    }

    /** Get the top element. */
    public int top() {
        if (!flag){
            Queue<Integer> temp = new LinkedList<Integer>();
            int top = this.queue.remove();
            while(!this.queue.isEmpty()){
                temp.add(top);
                top = this.queue.remove();
            }
            temp.add(top);
            this.queue = temp;
            this.flag = true;
            this.top = top;

        }
        return this.top;

    }

    /** Returns whether the stack is empty. */
    public boolean empty() {
        return this.queue.isEmpty();
    }
}

/**
 * Your MyStack object will be instantiated and called as such:
 * MyStack obj = new MyStack();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.top();
 * boolean param_4 = obj.empty();
 */