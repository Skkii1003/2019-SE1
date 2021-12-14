package com.njuse.jvmfinal.instructions.base;

import com.njuse.jvmfinal.runtime.StackFrame;

import java.nio.ByteBuffer;

public abstract class Instruction {
    public Instruction() {
    }

    public abstract void execute(StackFrame var1);

    public abstract void fetchOperands(ByteBuffer var1);
}
