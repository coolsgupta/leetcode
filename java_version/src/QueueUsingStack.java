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

// complexity push O(1), pop amortized O(1)
class MyQueueOptimized {
    Stack<Integer> stack1;
    Stack<Integer> stack2;
    int front;

    /** Initialize your data structure here. */
    public MyQueueOptimized() {
        this.stack1 = new Stack<Integer>();
        this.stack2 = new Stack<Integer>();
    }

    /** Push element x to the back of queue. */
    public void push(int x) {
        if(this.stack1.empty())
            front = x;
        this.stack1.push(x);
    }

    /** Removes the element from in front of queue and returns that element. */
    public int pop() {
        if(this.stack2.empty())
            while(!this.stack1.empty())
                this.stack2.push(this.stack1.pop());

        return this.stack2.pop();
    }

    /** Get the front element. */
    public int peek() {
        if(!this.stack2.empty())
            return this.stack2.peek();

        return front;
    }

    /** Returns whether the queue is empty. */
    public boolean empty() {
        return this.stack1.isEmpty() && this.stack2.isEmpty();
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