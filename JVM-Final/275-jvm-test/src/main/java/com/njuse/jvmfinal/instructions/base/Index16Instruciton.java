package com.njuse.jvmfinal.instructions.base;
import java.nio.ByteBuffer;

abstract class Index16Instruction extends Instruction {
    public int index;

    public Index16Instruction() {
    }

    public void fetchOperands(ByteBuffer reader) {
        this.index = reader.getShort() & '\uffff';
    }

    public String toString() {
        return this.getClass().getSimpleName() + " index: " + (this.index & '\uffff');
    }
}