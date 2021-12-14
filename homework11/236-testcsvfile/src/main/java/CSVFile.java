import java.io.*;

public class CSVFile {

	public static void main(String[] args) {
		String filePath = CSVFile.class.getClassLoader().getResource("data.txt").getPath();
		printCSVFile(filePath);
	}
	
	public static void printCSVFile(String filePath){
		//add code here
		try{
		    BufferedReader f = new BufferedReader(new FileReader(filePath));
		    String str;
		    System.out.println("Last    Fisrt    Salary");

		    do{
			    str = f.readLine();
			    String[] list = str.split(",");
			    System.out.println(list[0]+"    "+list[1]+"    "+list[2]);

		    }while(str != "");
	    }catch(Exception e){
		}
	}
	

}
