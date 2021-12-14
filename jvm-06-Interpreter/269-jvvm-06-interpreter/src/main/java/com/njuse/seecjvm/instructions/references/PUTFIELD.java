package com.njuse.seecjvm.instructions.references;

import com.njuse.seecjvm.instructions.base.Index16Instruction;
import com.njuse.seecjvm.memory.jclass.Field;
import com.njuse.seecjvm.memory.jclass.JClass;
import com.njuse.seecjvm.memory.jclass.Method;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.RuntimeConstantPool;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.ref.FieldRef;
import com.njuse.seecjvm.runtime.OperandStack;
import com.njuse.seecjvm.runtime.StackFrame;
import com.njuse.seecjvm.runtime.Vars;
import com.njuse.seecjvm.runtime.struct.JObject;
import com.njuse.seecjvm.runtime.struct.NonArrayObject;

import java.lang.annotation.IncompleteAnnotationException;


public class PUTFIELD extends Index16Instruction {
    /**
     * TODO 实现这条指令
     * 其中 对应的index已经读取好了
     */
    @Override
    public void execute(StackFrame frame) {
        Method method = frame.getMethod();
        JClass clazz = method.getClazz();
        RuntimeConstantPool current = clazz.getRuntimeConstantPool();
        FieldRef fieldRef = (FieldRef) current.getConstant(index);
        Field field;

        try{
            field = fieldRef.getResolvedFieldRef();
            JClass c = field.getClazz();
            if(field.isStatic()){
                throw new IncompatibleClassChangeError();
            }
            if(field.isFinal()){
                throw new IllegalAccessError();
            }

            String descriptor = field.getDescriptor();
            int id = field.getSlotID();
            OperandStack stack = frame.getOperandStack();
            JObject ref;
            switch (descriptor.charAt(0)){
                case 'B':
                case 'C':
                case 'Z':
                case 'S':
                case 'I':
                    int val1 = stack.popInt();
                    ref = stack.popObjectRef();
                    if(ref.isNull()) throw new NullPointerException();
                    ((NonArrayObject) ref).getFields().setInt(id,val1);
                    break;
                case 'F':
                    float val2 = stack.popFloat();
                    ref = stack.popObjectRef();
                    if(ref.isNull()) throw new NullPointerException();
                    ((NonArrayObject) ref).getFields().setFloat(id,val2);
                    break;
                case 'J':
                    long val3 = stack.popLong();
                    ref = stack.popObjectRef();
                    if(ref.isNull()) throw new NullPointerException();
                    ((NonArrayObject) ref).getFields().setLong(id,val3);
                    break;
                case 'D':
                    double val4 = stack.popDouble();
                    ref = stack.popObjectRef();
                    if(ref.isNull()) throw new NullPointerException();
                    ((NonArrayObject) ref).getFields().setDouble(id,val4);
                    break;
                case 'L':
                case '[':
                    JObject val5 = stack.popObjectRef();
                    ref = stack.popObjectRef();
                    if(ref.isNull()) throw new NullPointerException();
                    ((NonArrayObject) ref).getFields().setObjectRef(id,val5);
                    break;
            }
        }catch(ClassNotFoundException e){
            e.printStackTrace();
        }
    }

}
