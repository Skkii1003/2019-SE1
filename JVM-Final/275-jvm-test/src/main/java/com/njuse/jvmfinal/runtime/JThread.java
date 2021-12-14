package com.njuse.jvmfinal.runtime;

public class JThread {
    private ThreadStack stack = new ThreadStack();

    public JThread() {
    }

    public void pushFrame(StackFrame frame) {
        this.stack.pushFrame(frame);
    }

    public void popFrame() {
        this.stack.popFrame();
    }

    public StackFrame getTopFrame() {
        return this.stack.getTopFrame();
    }

    public ThreadStack getStack() {
        return this.stack;
    }

    public void setStack(ThreadStack stack) {
        this.stack = stack;
    }
}
