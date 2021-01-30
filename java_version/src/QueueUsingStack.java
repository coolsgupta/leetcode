public class QueueUsingStack {
    Stack<Integer> stack;

    /** Initialize your data structure here. */
    public MyQueue() {
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
