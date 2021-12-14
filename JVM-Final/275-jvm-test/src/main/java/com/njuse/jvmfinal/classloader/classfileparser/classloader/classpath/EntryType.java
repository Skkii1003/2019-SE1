package com.njuse.jvmfinal.classloader.classfileparser.classloader.classpath;

public class EntryType {
    private int value;
    public static final int BOOT_ENTRY = 1;
    public static final int EXT_ENTRY = 3;
    public static final int USER_ENTRY = 7;

    public EntryType(int value) {
        this.value = value;
    }

    public int getValue() {
        return this.value;
    }
}
