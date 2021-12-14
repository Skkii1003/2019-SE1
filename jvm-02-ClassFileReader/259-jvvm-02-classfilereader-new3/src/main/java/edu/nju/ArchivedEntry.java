package edu.nju;

//import jdk.internal.util.xml.impl.Input;

//import java.io.File
import java.io.FileInputStream;
import java.io.IOException;
import java.io.InputStream;
import java.util.jar.JarEntry;
import java.util.jar.JarFile;
import java.util.jar.JarInputStream;
import java.util.zip.ZipEntry;
import java.util.zip.ZipFile;
import java.util.zip.ZipInputStream;

/**
 * format : dir/subdir/target.jar
 */
public class ArchivedEntry extends Entry{
    public ArchivedEntry(String classpath) {
        super(classpath);
    }

    @Override
    public byte[] readClassFile(String className) throws IOException {

        if(classpath.contains(".jar")||classpath.contains(".JAR")){
            JarInputStream jar = new JarInputStream(new FileInputStream(classpath));
            JarEntry entry = null;
            while((entry = jar.getNextJarEntry())!= null){
                String name = entry.getName();

                if(name.equals(className)){
                    JarFile jarfile = new JarFile(classpath);
                    InputStream in = jarfile.getInputStream(entry);
                    return IOUtil.readFileByBytes(in);
                }
            }
        }
        else{
            ZipInputStream zip = new ZipInputStream(new FileInputStream(classpath));
            ZipEntry entry = null;
            while((entry = zip.getNextEntry())!= null){
                String name = entry.getName();
                if(name.equals(className)){
                    ZipFile zipfile = new ZipFile(classpath);
                    InputStream in = zipfile.getInputStream(entry);
                    return IOUtil.readFileByBytes(in);
                }
            }
        }
        return null;
    }
}
