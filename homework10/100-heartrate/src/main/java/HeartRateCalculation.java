import java.util.Scanner;

public class HeartRateCalculation {

	public static void main(String[] args) {
		int age;
		int targetHR;
		int restingHR;
		double intensity;

		//input 1
		System.out.println("RestingHR:");
		Scanner input = new Scanner(System.in);
        String temp1 = input.nextLine();
        restingHR = Integer.parseInt(temp1);

        //input 2
		System.out.println("Age:");
		String temp2 = input.nextLine();
		age = Integer.parseInt(temp2);

		//process and output
		System.out.println("Intensity|TargetHeartRate");
		System.out.println("---------|---------------");
		for(intensity = 0.55;intensity <1.0;intensity = intensity + 0.05){
		    targetHR = (int) ((220 - age - restingHR) * intensity + restingHR + 0.5);

		    System.out.println((int)(intensity*100) + "%      |" + targetHR + "bpm         ");
		}
	}
}
