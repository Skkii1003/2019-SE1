package com.njuse.seecjvm.instructions.references;

import com.njuse.seecjvm.instructions.base.Index16Instruction;
import com.njuse.seecjvm.memory.JHeap;
import com.njuse.seecjvm.memory.jclass.InitState;
import com.njuse.seecjvm.memory.jclass.JClass;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.RuntimeConstantPool;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.ref.ClassRef;
import com.njuse.seecjvm.runtime.StackFrame;
import com.njuse.seecjvm.runtime.struct.NonArrayObject;

public class NEW extends Index16Instruction {
    /**
     * TODO 实现这条指令
     * 其中 对应的index已经读取好了
     */
    @Override
    public void execute(StackFrame frame) {
        RuntimeConstantPool run = frame.getMethod().getClazz().getRuntimeConstantPool();
        ClassRef ref = (ClassRef) run.getConstant(index);

        try{
            JClass clazz = ref.getResolvedClass();
            if(clazz.getInitState()== InitState.PREPARED){
                frame.setNextPC(frame.getNextPC()-3);
                clazz.initClass(frame.getThread(),clazz);
                return;
            }

            if(clazz.isInterface()||clazz.isAbstract()) throw new InstantiationError();

            NonArrayObject oref = clazz.newObject();
            JHeap.getInstance().addObj(oref);
            frame.getOperandStack().pushObjectRef(oref);
        }catch(ClassNotFoundException e){
            e.printStackTrace();
        }
    }
}
