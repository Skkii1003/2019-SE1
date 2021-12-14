package com.njuse.jvmfinal.classloader.classfileparser.classloader.classpath;

import java.io.File;
import java.io.IOException;

public class CompositeEntry extends Entry{
    public CompositeEntry(String classpath) {
        super(classpath);
    }

    public byte[] readClassFile(String className) throws IOException {

        String[] path = classpath.split(File.pathSeparator);

        for(int i=0;i<path.length;i++){
            if(path[i].contains("*")){
                WildEntry w = new WildEntry(path[i]);
                byte[] result = w.readClassFile(className);
                if(result!=null){
                    return result;
                }
            }
            else if(path[i].contains(".jar")||path[i].contains(".JAR")||path[i].contains(".zip")||path[i].contains(".ZIP")){
                ArchivedEntry a = new ArchivedEntry(path[i]);
                byte[] result = a.readClassFile(className);
                if(result!=null){
                    return result;
                }
            }
            else{
                DirEntry d = new DirEntry(path[i]);
                byte[] result = d.readClassFile(className);
                if(result!=null){
                    return result;
                }
            }
        }
        return null;
    }
}