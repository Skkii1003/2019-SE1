import java.util.Scanner;
public class CompareNumbers {

	public static void main(String[] args) {
		int one = 0;
		int two = 0;
		int three = 0;

        //input
		System.out.println("Enter the first number:");
		Scanner input = new Scanner(System.in);
		String strone = input.nextLine();
		one = Integer.parseInt(strone);

		System.out.println("Enter the second number:");
		String strtwo = input.nextLine();
		two = Integer.parseInt(strtwo);

		System.out.println("Enter the third number:");
		String strthree = input.nextLine();
		three = Integer.parseInt(strthree);

		//compare
		if(one == two || one == three || two == three){
			System.out.println("There are same numbers.");
		}else{
			if(one>two & one>three){
				System.out.println("The largest number is "+one+".");
			}else if(two>one & two>three){
				System.out.println("The largest number is "+two+".");
			}else{
				System.out.println("The largest number is "+three+".");
			}
		}

	}

}
