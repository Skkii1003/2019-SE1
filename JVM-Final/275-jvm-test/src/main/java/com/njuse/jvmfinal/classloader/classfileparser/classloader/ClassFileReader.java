package com.njuse.jvmfinal.classloader.classfileparser.classloader;

import com.njuse.jvmfinal.classloader.classfileparser.classloader.classpath.*;
import org.apache.commons.lang3.tuple.Pair;

import java.io.File;
import java.io.IOException;

public class ClassFileReader {
    private static final String FILE_SEPARATOR = File.separator;
    private static final String PATH_SEPARATOR = File.pathSeparator;
    private static ClassFileReader reader = new ClassFileReader();

    private ClassFileReader(){

    }

    public static ClassFileReader getInstance(){ return reader;}

    private static Entry bootClasspath = null;
    private static Entry extClasspath = null;
    private static Entry userClasspath = null;

    public static Entry chooseEntryType(String classpath) {
        if(classpath==null)
            return null;
        if(classpath.contains(File.pathSeparator))
            return new CompositeEntry(classpath);
        else if(classpath.endsWith("*"))
            return new WildEntry(classpath);
        else if (classpath.endsWith("jar")||classpath.endsWith("JAR")||classpath.endsWith("zip")||classpath.endsWith("ZIP"))
            return new ArchivedEntry(classpath);
        else
            return new DirEntry(classpath);
    }

    public Pair<byte[], Integer> readClassFile(String className, EntryType privilege) throws IOException,ClassNotFoundException{
        String name = className + ".class";
        if(name.contains("/"))
            name.replace("/",File.separator);

        byte[] contents = null;
        int value;

        if(privilege==null)
            value = EntryType.USER_ENTRY;
        else
            value = privilege.getValue();

        if(value>=EntryType.BOOT_ENTRY){
            contents = bootClasspath.readClassFile(name);

            if(contents!=null)
                return Pair.of(contents,EntryType.BOOT_ENTRY);

        }
        else if(value>=EntryType.EXT_ENTRY){
            contents = extClasspath.readClassFile(name);

            if(contents!=null)
                return Pair.of(contents,EntryType.EXT_ENTRY);
        }
        else if(value>=EntryType.USER_ENTRY){
            contents = userClasspath.readClassFile(name);

            if(contents!=null)
                return Pair.of(contents,EntryType.USER_ENTRY);
        }
        else
            throw new ClassNotFoundException();

        return Pair.of(contents,value);
    }


}
