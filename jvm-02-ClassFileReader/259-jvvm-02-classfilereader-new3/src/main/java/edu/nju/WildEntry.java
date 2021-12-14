package edu.nju;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.jar.JarInputStream;

/**
 * format : dir/.../*
 */
public class WildEntry extends Entry{
    public WildEntry(String classpath) {
        super(classpath);
    }

    @Override
    public byte[] readClassFile(String className) throws IOException {
        classpath = classpath.substring(0,classpath.length()-1);
        File f = new File(classpath.substring(0,classpath.length()-1));
        String[] flist = f.list();

        assert flist != null;
        for(int i = 0; i<flist.length&&flist[i].contains("jar")||flist[i].contains("JAR"); i++){
            JarInputStream jar = new JarInputStream(new FileInputStream(classpath+flist[i]));

            JarEntry entry = null;
            while((entry = jar.getNextJarEntry())!= null){
                String name = entry.getName();

                if(name.equals(className)){
                    JarFile jarfile = new JarFile(classpath+flist[i]);
                    InputStream in = jarfile.getInputStream(entry);
                    return IOUtil.readFileByBytes(in);
                }
            }
        }
        return null;
    }
}
