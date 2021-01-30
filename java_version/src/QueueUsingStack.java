public class QueueUsingStack {
    Stack<Integer> stack;

    /** Initialize your data structure here. */
    public QueueUsingStack() {
        this.stack = new Stack<Integer>();

    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        Stack<Integer> temp = new Stack<Integer>();
        while(!this.stack.isEmpty())
            temp.push(this.stack.pop());

        this.stack.push(x);

        while(!temp.isEmpty())
            this.stack.push(temp.pop());
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        return this.stack.pop();
    }

    /** Get the front element. */
    public int peek() {
        return this.stack.peek();
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return this.stack.isEmpty();
    }
}

/**
 * Your MyQueue object will be instantiated and called as such:
 * MyQueue obj = new MyQueue();
 * obj.push(x);
 * int param_2 = obj.pop();
 * int param_3 = obj.peek();
 * boolean param_4 = obj.empty();
 */