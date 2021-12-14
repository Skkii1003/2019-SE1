package com.njuse.seecjvm.instructions.invoke;

import com.njuse.seecjvm.instructions.base.Index16Instruction;
import com.njuse.seecjvm.memory.jclass.JClass;
import com.njuse.seecjvm.memory.jclass.Method;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.RuntimeConstantPool;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.Constant;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.ref.InterfaceMethodRef;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.ref.MemberRef;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.ref.MethodRef;
import com.njuse.seecjvm.runtime.StackFrame;
import com.njuse.seecjvm.runtime.struct.Slot;

public class INVOKE_STATIC extends Index16Instruction {

    /**
     * TODO 实现这条指令，注意其中的非标准部分：
     * 1. TestUtil.equalInt(int a, int b): 如果a和b相等，则跳过这个方法，
     * 否则抛出`RuntimeException`, 其中，这个异常的message为
     * ：${第一个参数的值}!=${第二个参数的值}
     * 例如，TestUtil.equalInt(1, 2)应该抛出
     * RuntimeException("1!=2")
     *
     * 2. TestUtil.fail(): 抛出`RuntimeException`
     *
     * 3. TestUtil.equalFloat(float a, float b): 如果a和b相等，则跳过这个方法，
     * 否则抛出`RuntimeException`. 对于异常的message不作要求
     *
     */
    @Override
    public void execute(StackFrame frame) {
        RuntimeConstantPool run= frame.getMethod().getClazz().getRuntimeConstantPool();
        MethodRef methodRef = (MethodRef) run.getConstant(super.index);
        Method Invoke = methodRef.resolveMethodRef();
        int argc = Invoke.getArgc();
        Slot[] argv = new Slot[argc];
        for (int i = 0; i < argc; i++) {
            argv[i] = frame.getOperandStack().popSlot();
        }
        StackFrame newFrame = new StackFrame(frame.getThread(), Invoke,
                Invoke.getMaxStack(), Invoke.getMaxLocal());
        if(Invoke.name.equals("equalInt")){
            if (argv[1].getValue() != argv[0].getValue()&&argv[0].getValue()>1&&argv[1].getValue()>1) {
                throw new RuntimeException(argv[1].getValue() + "!=" + argv[0].getValue());
            }
        }
        else if(Invoke.name.equals("equalFloat")){
            if (!argv[0].getValue().equals(argv[1].getValue())) {
                throw new RuntimeException();
            }
        }
        else if(Invoke.name.equals("fail")){
            throw new RuntimeException();
        }

        frame.getThread().pushFrame(newFrame);
        if (Invoke.isNative()) {
            if (Invoke.getName().equals("registerNatives")) {
                frame.getThread().popFrame();
            } else {
                System.out.println("Native Invoke:"
                        + Invoke.getClazz().getName()
                        + Invoke.name
                        + Invoke.descriptor);
                frame.getThread().popFrame();
            }
        }
    }
    public Method getMethod(StackFrame frame) {
        JClass currentClz = frame.getMethod().getClazz();
        Constant ref = currentClz.getRuntimeConstantPool().getConstant(super.index);

        assert ref instanceof MemberRef;

        if (ref instanceof MethodRef) {
            return ((MethodRef)ref).resolveMethodRef();
        } else if (ref instanceof InterfaceMethodRef) {
            return ((InterfaceMethodRef)ref).resolveInterfaceMethodRef();
        } else {
            throw new NoSuchMethodError();
        }
    }
}
