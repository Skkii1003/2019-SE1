package com.njuse.jvmfinal.instructions.constant;

import com.njuse.jvmfinal.instructions.base.NoOperandsInstruction;
import com.njuse.jvmfinal.runtime.StackFrame;

public class ICONST_N extends NoOperandsInstruction {
    private int val;
    private static int[] valid = new int[]{-1, 0, 1, 2, 3, 4, 5};

    public ICONST_N(int val) {
        if (val >= valid[0] && val <= valid[valid.length - 1]) {
            this.val = val;
        } else {
            throw new IllegalArgumentException();
        }
    }

    public void execute(StackFrame frame) {
        frame.getOperandStack().pushInt(this.val);
    }

    public String toString() {
        String suffix = this.val == -1 ? "M1" : "" + this.val;
        String simpleName = this.getClass().getSimpleName();
        return simpleName.substring(0, simpleName.length() - 1) + suffix;
    }
}
