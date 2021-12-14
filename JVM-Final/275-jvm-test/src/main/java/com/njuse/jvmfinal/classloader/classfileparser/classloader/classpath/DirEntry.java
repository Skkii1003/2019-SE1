package com.njuse.jvmfinal.classloader.classfileparser.classloader.classpath;

import java.io.File;
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import com.njuse.jvmfinal.util.IOUtil;

public class DirEntry extends Entry{
    public DirEntry(String classpath) {
        super(classpath);
    }

    @Override
    public byte[] readClassFile(String className) throws IOException {
        className = IOUtil.delete(className);

        File f = new File(classpath);
        String[] flist = f.list();
        if(flist == null)
            return null;
        for(int i = 0; i<flist.length; i++){

            if(flist[i].equals(className)){
                File file = new File(classpath+File.separator+className);
                InputStream in = new FileInputStream(file);
                return IOUtil.readFileByBytes(in);
            }
        }
        return null;
    }
}
