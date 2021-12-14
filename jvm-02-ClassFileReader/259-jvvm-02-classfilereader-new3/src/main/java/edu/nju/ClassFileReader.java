package edu.nju;

import java.io.File;
import java.io.IOException;

public class ClassFileReader {
    private static final String FILE_SEPARATOR = File.separator;
    private static final String PATH_SEPARATOR = File.pathSeparator;

    private static Entry bootStrapReader;

    public static Entry chooseEntryType(String classpath) {
        /**
         * tips:
         *      Every case can correspond to a class
         *      These cases are disordered
         *      You should take care of the order of if-else
         * case 1 classpath with wildcard
         * case 2 normal dir path
         * case 3 archived file
         * case 4 classpath with path separator
         */
        if(classpath==null)
            return null;

        DirEntry d = new DirEntry(classpath);
        ArchivedEntry a = new ArchivedEntry(classpath);
        WildEntry w = new WildEntry(classpath);
        CompositeEntry c = new CompositeEntry(classpath);

        if(classpath.contains(File.pathSeparator))
            return c;
        else if(classpath.contains("*"))
            return w;
        else if (classpath.contains("jar")||classpath.contains("JAR")||classpath.contains("zip")||classpath.contains("ZIP"))
            return a;
        else
            return d;
    }

    /**
     *
     * @param classpath where to find target class
     * @param className format: /package/.../class
     * @return content of classfile
     */
    public static byte[] readClassFile(String classpath,String className) throws ClassNotFoundException{
        className += ".class";
        bootStrapReader = chooseEntryType(classpath);
        if (bootStrapReader==null)throw new ClassNotFoundException();
        byte[] ret = new byte[0];
        try {
            ret = bootStrapReader.readClassFile(className);
        } catch (IOException e) {
            e.printStackTrace();
        }
        if (ret==null)throw new ClassNotFoundException();
        return ret;
    }
}
