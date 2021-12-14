package com.njuse.seecjvm.instructions.comparison;

import com.njuse.seecjvm.instructions.base.NoOperandsInstruction;
import com.njuse.seecjvm.runtime.StackFrame;

public class DCMPL extends NoOperandsInstruction {

    /**
     * TODO：实现这条指令
     */
    @Override
    public void execute(StackFrame frame) {
        double val1 = frame.getOperandStack().popDouble();
        double val2 = frame.getOperandStack().popDouble();
        if(val2 > val1){
            frame.getOperandStack().pushInt(1);
        }
        else if(val1 == val2){
            frame.getOperandStack().pushInt(0);
        }
        else if(val2 < val1){
            frame.getOperandStack().pushInt(-1);
        }
        else
            frame.getOperandStack().pushInt(-1);
    }
}
