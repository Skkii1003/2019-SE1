package com.njuse.seecjvm.instructions.control;

import com.njuse.seecjvm.instructions.base.NoOperandsInstruction;
import com.njuse.seecjvm.runtime.JThread;
import com.njuse.seecjvm.runtime.StackFrame;

public class IRETURN extends NoOperandsInstruction {

    /**
     * TODO： 实现这条指令
     */
    @Override
    public void execute(StackFrame frame) {
        int val = frame.getOperandStack().popInt();
        JThread thread = frame.getThread();
        thread.popFrame();
        thread.getTopFrame().getOperandStack().pushInt(val);
    }
}
