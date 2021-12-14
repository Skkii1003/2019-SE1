package com.njuse.jvmfinal.memory.jclass;

import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public abstract class ClassMember {
    public short accessFlags;
    public String name;
    public String descriptor;
    public JClass clazz;

    public ClassMember() {
    }

    public boolean isStatic() {
        return 0 != (this.accessFlags & 8);
    }
    public boolean isLongOrDouble() {
        return this.descriptor.equals("J") || this.descriptor.equals("D");
    }
    public boolean isFinal() {
        return 0 != (this.accessFlags & 16);
    }
}
