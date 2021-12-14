package edu.nju;

import org.apache.commons.cli.*;

import java.io.IOException;

public class CommandLineUtil {
    private static CommandLine commandLine;
    private static CommandLineParser parser = new DefaultParser();
    private static Options options = new Options();
    private boolean sideEffect ;
    public static final String WRONG_MESSAGE = "Invalid input.";

    /**
     * you can define options here
     * or you can create a func such as [static void defineOptions()] and call it before parse input
     */
    static void defineOptions(){
        options.addOption(new Option("h",false,"打印出所有预定义的选项与用法"));
        options.addOption(new Option("p",true,"打印出arg"));
        options.addOption(new Option("s",false,"将CommandlineUnit中sideEffect变量置为true"));
    }

    public void main(String[] args) {
        defineOptions();
        parseInput(args);
    }


    /**
     * Print the usage of all options
     */
//    private static void printHelpMessage() {
//        String header = "header of help message";
//        String footer = "footer of help message";
//
//        HelpFormatter formatter = new HelpFormatter();
//        formatter.printHelp("myapp",header,options,footer);
//    }
    private static void printHelpMessage(){
        System.out.println("help");
    }
    /**
     * Parse the input and handle exception
     * @param args origin args form input
     */
    public void parseInput(String[] args) {
        try {
            CommandLine cmd = parser.parse(options, args);

            // check whether has h
            if (cmd.hasOption("h")) {
                printHelpMessage();
                return;
            }

            // check whether has p and s
            else {
                if(cmd.getArgs().length == 0){
                    System.out.println(WRONG_MESSAGE);
                    return;
                }

                if (cmd.hasOption("s")) {
                    sideEffect = true;
                }
                else
                    sideEffect = false;

                if (cmd.hasOption("p")) {
                    System.out.println(cmd.getOptionValue("p"));
                }
            }
        }catch(ParseException e){
            System.out.println(e.getMessage());
            System.exit(-1);
        }
    }


    /**
     * You can handle options here or create your own func
     */


    public boolean getSideEffectFlag(){
        return sideEffect;
    }

}
