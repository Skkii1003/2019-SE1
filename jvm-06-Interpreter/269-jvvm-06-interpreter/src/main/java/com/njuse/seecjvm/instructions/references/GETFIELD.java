package com.njuse.seecjvm.instructions.references;

import com.njuse.seecjvm.instructions.base.Index16Instruction;
import com.njuse.seecjvm.memory.jclass.Field;
import com.njuse.seecjvm.memory.jclass.JClass;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.RuntimeConstantPool;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.ref.FieldRef;
import com.njuse.seecjvm.runtime.OperandStack;
import com.njuse.seecjvm.runtime.StackFrame;
import com.njuse.seecjvm.runtime.Vars;
import com.njuse.seecjvm.runtime.struct.NonArrayObject;

public class GETFIELD extends Index16Instruction {

    /**
     * TODO 实现这条指令
     * 其中 对应的index已经读取好了
     */
    @Override
    public void execute(StackFrame frame) {
        RuntimeConstantPool current = frame.getMethod().getClazz().getRuntimeConstantPool();
        FieldRef fieldRef = (FieldRef) current.getConstant(index);
        Field field;

        try{
            field = fieldRef.getResolvedFieldRef();
            JClass clazz = field.getClazz();
            if(field.isStatic()){
                throw new IncompatibleClassChangeError();
            }
            OperandStack stack = frame.getOperandStack();
            NonArrayObject ref = (NonArrayObject) stack.popObjectRef();

            if(ref.isNull()){
                throw new NullPointerException();
            }
            String descriptor = field.getDescriptor();
            int id = field.getSlotID();
            Vars fields = ref.getFields();
            switch (descriptor.charAt(0)){
                case 'B':
                case 'C':
                case 'Z':
                case 'S':
                case 'I':
                    stack.pushInt(fields.getInt(id));
                    break;
                case 'F':
                    stack.pushFloat(fields.getFloat(id));
                    break;
                case 'J':
                    stack.pushLong(fields.getLong(id));
                    break;
                case 'D':
                    stack.pushDouble(fields.getDouble(id));
                    break;
                case 'L':
                case '[':
                    stack.pushObjectRef(fields.getObjectRef(id));
                    break;
            }
        }catch(ClassNotFoundException e){
            e.printStackTrace();
        }
    }
}
