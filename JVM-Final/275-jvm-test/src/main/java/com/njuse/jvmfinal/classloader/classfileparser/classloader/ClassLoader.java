package com.njuse.jvmfinal.classloader.classfileparser.classloader;

import com.njuse.jvmfinal.classloader.classfileparser.ClassFile;
import com.njuse.jvmfinal.classloader.classfileparser.classloader.classpath.EntryType;
import com.njuse.jvmfinal.memory.jclass.Field;
import com.njuse.jvmfinal.memory.jclass.InitState;
import com.njuse.jvmfinal.memory.jclass.JClass;
import com.njuse.jvmfinal.memory.jclass.MethodArea;
import com.njuse.jvmfinal.memory.jclass.runtimeConstantPool.RuntimeConstantPool;
import com.njuse.jvmfinal.memory.jclass.runtimeConstantPool.constant.wrapper.DoubleWrapper;
import com.njuse.jvmfinal.memory.jclass.runtimeConstantPool.constant.wrapper.FloatWrapper;
import com.njuse.jvmfinal.memory.jclass.runtimeConstantPool.constant.wrapper.IntWrapper;
import com.njuse.jvmfinal.memory.jclass.runtimeConstantPool.constant.wrapper.LongWrapper;
import com.njuse.jvmfinal.runtime.Vars;
import com.njuse.jvmfinal.runtime.struct.NullObject;
import org.apache.commons.lang3.tuple.Pair;

import java.io.IOException;

public class ClassLoader {
    private static ClassLoader classLoader = new ClassLoader();
    private ClassFileReader classFileReader;
    private MethodArea methodArea;

    private ClassLoader() {
        classFileReader = ClassFileReader.getInstance();
        methodArea = MethodArea.getInstance();
    }

    public static ClassLoader getInstance() {
        return classLoader;
    }

    public JClass loadClass(String className, EntryType initiatingEntry) throws ClassNotFoundException {
        JClass ret;
        if ((ret = methodArea.findClass(className)) == null) {
            if(className.charAt(0)=='[')
                return this.loadArrayClass(className,initiatingEntry);
            else
                return this.loadNonArrayClass(className,initiatingEntry);

        }
        else
            return ret;
    }
    private JClass loadNonArrayClass(String className, EntryType initiatingEntry) throws ClassNotFoundException {
        try {
            Pair<byte[], Integer> res = classFileReader.readClassFile(className, initiatingEntry);
            byte[] data = res.getKey();
            EntryType definingEntry = new EntryType(res.getValue());
            JClass clazz = defineClass(data, definingEntry);
            linkClass(clazz);
            return clazz;
        } catch (IOException e) {
            e.printStackTrace();
            throw new ClassNotFoundException();
        }
    }

    private JClass loadArrayClass(String className, EntryType initiatingEntry) {
        JClass ret = new JClass();
        ret.setAccessFlags((short)1);
        ret.setName(className);
        ret.setInitState(InitState.SUCCESS);
        this.methodArea.addClass(ret.getName(), ret);

        try {
            ret.setSuperClass(this.tryLoad("java/lang/Object", initiatingEntry));
            JClass[] interfaces = new JClass[]{this.tryLoad("java/lang/Cloneable", initiatingEntry), this.tryLoad("java/io/Serializable", initiatingEntry)};
            ret.setInterfaces(interfaces);
        } catch (ClassNotFoundException e) {
            e.printStackTrace();
        }

        return ret;
    }

    private JClass defineClass(byte[] data, EntryType definingEntry) throws ClassNotFoundException {
        ClassFile classFile = new ClassFile(data);
        JClass clazz = new JClass(classFile);
        clazz.setLoadEntryType(definingEntry);
        resolveSuperClass(clazz);
        resolveInterfaces(clazz);
        methodArea.addClass(clazz.getName(),clazz);
        return clazz;
    }

    private JClass tryLoad(String className, EntryType initiatingEntry) throws ClassNotFoundException {
        JClass ret;
        return (ret = this.methodArea.findClass(className)) == null ? this.loadNonArrayClass(className, initiatingEntry) : ret;
    }

    private void resolveSuperClass(JClass clazz) throws ClassNotFoundException {
        if (!clazz.getName().equals("java/lang/Object")) {
            String superClassName = clazz.getSuperClassName();
            EntryType initiatingEntry = clazz.getLoadEntryType();
            clazz.setSuperClass(this.loadClass(superClassName, initiatingEntry));
        }
    }

    private void resolveInterfaces(JClass clazz) throws ClassNotFoundException {
        EntryType initiatingEntry = clazz.getLoadEntryType();
        String[] interfaceNames = clazz.getInterfaceNames();
        int interfaceCount = interfaceNames.length;
        JClass[] interfaces = new JClass[interfaceCount];
        clazz.setInterfaces(interfaces);

        for(int i = 0; i < interfaceCount; ++i) {
            interfaces[i] = this.loadClass(interfaceNames[i], initiatingEntry);
        }
    }

    private void linkClass(JClass clazz) {
        this.verify(clazz);
        this.prepare(clazz);
    }

    private void verify(JClass clazz) {
    }

    private void prepare(JClass clazz) {
        this.calInstanceFieldSlotIDs(clazz);
        this.calStaticFieldSlotIDs(clazz);
        this.allocAndInitStaticVars(clazz);
        clazz.setInitState(InitState.PREPARED);
    }

    private void calInstanceFieldSlotIDs(JClass clazz) {
        int slotID = 0;
        if (clazz.getSuperClass() != null) {
            slotID = clazz.getSuperClass().getInstanceSlotCount();
        }

        Field[] fields = clazz.getFields();
        Field[] var1 = fields;
        int var2 = fields.length;

        for(int i = 0; i < var2; ++i) {
            Field f = var1[i];
            if (!f.isStatic()) {
                f.setSlotID(slotID);
                ++slotID;
                if (f.isLongOrDouble()) {
                    ++slotID;
                }
            }
        }

        clazz.setInstanceSlotCount(slotID);
    }
    private void calStaticFieldSlotIDs(JClass clazz) {
        int slotID = 0;
        Field[] fields = clazz.getFields();
        Field[] var1 = fields;
        int var2 = fields.length;

        for(int i = 0; i < var2; ++i) {
            Field f = var1[i];
            if (f.isStatic()) {
                f.setSlotID(slotID);
                ++slotID;
                if (f.isLongOrDouble()) {
                    ++slotID;
                }
            }
        }

        clazz.setStaticSlotCount(slotID);
    }

    private void allocAndInitStaticVars(JClass clazz) {
        clazz.setStaticVars(new Vars(clazz.getStaticSlotCount()));
        Field[] fields = clazz.getFields();
        Field[] var1 = fields;
        int var2 = fields.length;

        for(int i = 0; i < var2; ++i) {
            Field f = var1[i];
            if (f.isStatic() && f.isFinal()) {
                this.loadValueFromRTCP(clazz, f);
            } else if (f.isStatic()) {
                this.initDefaultValue(clazz, f);
            }
        }
    }

    private void loadValueFromRTCP(JClass clazz, Field field) {
        Vars staticVars = clazz.getStaticVars();
        RuntimeConstantPool runtimeConstantPool = clazz.getRuntimeConstantPool();
        int constantPoolIndex = field.getConstValueIndex();
        int slotID = field.getSlotID();
        if (constantPoolIndex > 0) {
            String var7 = field.getDescriptor();
            byte var8 = -1;
            switch(var7.hashCode()) {
                case 66:
                    if (var7.equals("B")) {
                        var8 = 1;
                    }
                    break;
                case 67:
                    if (var7.equals("C")) {
                        var8 = 2;
                    }
                    break;
                case 68:
                    if (var7.equals("D")) {
                        var8 = 6;
                    }
                case 69:
                case 71:
                case 72:
                case 75:
                case 76:
                case 77:
                case 78:
                case 79:
                case 80:
                case 81:
                case 82:
                case 84:
                case 85:
                case 86:
                case 87:
                case 88:
                case 89:
                default:
                    break;
                case 70:
                    if (var7.equals("F")) {
                        var8 = 7;
                    }
                    break;
                case 73:
                    if (var7.equals("I")) {
                        var8 = 4;
                    }
                    break;
                case 74:
                    if (var7.equals("J")) {
                        var8 = 5;
                    }
                    break;
                case 83:
                    if (var7.equals("S")) {
                        var8 = 3;
                    }
                    break;
                case 90:
                    if (var7.equals("Z")) {
                        var8 = 0;
                    }
            }

            switch(var8) {
                case 0:
                case 1:
                case 2:
                case 3:
                case 4:
                    int intVal = ((IntWrapper)runtimeConstantPool.getConstant(constantPoolIndex)).getValue();
                    staticVars.setInt(slotID, intVal);
                    break;
                case 5:
                    long longVal = ((LongWrapper)runtimeConstantPool.getConstant(constantPoolIndex)).getValue();
                    staticVars.setLong(slotID, longVal);
                    break;
                case 6:
                    double doubleVal = ((DoubleWrapper)runtimeConstantPool.getConstant(constantPoolIndex)).getValue();
                    staticVars.setDouble(slotID, doubleVal);
                    break;
                case 7:
                    float floatVal = ((FloatWrapper)runtimeConstantPool.getConstant(constantPoolIndex)).getValue();
                    staticVars.setFloat(slotID, floatVal);
            }
        }
    }

    private void initDefaultValue(JClass clazz, Field field) {
        Vars staticVars = clazz.getStaticVars();
        int slotID = field.getSlotID();
        String descriptor = field.getDescriptor();
        switch(descriptor.charAt(0)) {
            case 'B':
            case 'C':
            case 'I':
            case 'S':
            case 'Z':
                staticVars.setInt(slotID, 0);
                break;
            case 'D':
                staticVars.setDouble(slotID, 0.0D);
                break;
            case 'E':
            case 'G':
            case 'H':
            case 'K':
            case 'L':
            case 'M':
            case 'N':
            case 'O':
            case 'P':
            case 'Q':
            case 'R':
            case 'T':
            case 'U':
            case 'V':
            case 'W':
            case 'X':
            case 'Y':
            default:
                staticVars.setObjectRef(slotID, new NullObject());
                break;
            case 'F':
                staticVars.setFloat(slotID, 0.0F);
                break;
            case 'J':
                staticVars.setLong(slotID, 0L);
        }
    }
}
