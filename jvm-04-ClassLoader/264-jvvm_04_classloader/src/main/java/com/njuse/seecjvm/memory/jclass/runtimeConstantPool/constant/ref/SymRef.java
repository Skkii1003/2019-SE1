package com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.ref;

import com.njuse.seecjvm.classloader.ClassLoader;
import com.njuse.seecjvm.memory.jclass.JClass;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.RuntimeConstantPool;
import com.njuse.seecjvm.memory.jclass.runtimeConstantPool.constant.Constant;
import lombok.Getter;
import lombok.Setter;

@Getter
@Setter
public abstract class SymRef implements Constant {
    public RuntimeConstantPool runtimeConstantPool;
    public String className;    //format : java/lang/Object
    public JClass clazz;

    public void resolveClassRef() throws ClassNotFoundException, IllegalAccessException {
        //todo
        /**
         * Add some codes here.
         *
         * You can get a Jclass from runtimeConstantPool.getClazz()
         *
         * step 1
         * Complete the method isAccessibleTo() in Jclass
         * Make sure you know what is caller and what is callee.
         *
         * step2
         * Use ClassLoader.getInstance() to get the classloader
         * You should load class or interface C with initiating Loader of D
         *
         * step3
         * Check the permission and throw IllegalAccessException
         * Don't forget to set the value of clazz with loaded class
         */
        JClass D = runtimeConstantPool.getClazz();
        JClass C = ClassLoader.getInstance().loadClass(className,D.getLoadEntryType());
        if(!C.isAccessibleTo(D)){
            throw new IllegalAccessException(className+" is not accessible to "+D.getName());
        }
        clazz = C;
    }
}
