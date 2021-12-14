import java.util.*;
public class ResponseTimeCalculation {
	ArrayList<Integer> list = new ArrayList<Integer>();

	public static void main(String[] args){

			Scanner in = new Scanner(System.in);
			String str = "";
			ArrayList<Integer> nums = new ArrayList<Integer>();
			ResponseTimeCalculation method = new ResponseTimeCalculation();
			nums = method.list;
			int i = 0;

			do {
				System.out.println("Enter a Number:");
				str = in.next();
				if (str.equals("done")){
					break;
				}
				nums.add(Integer.parseInt(str));
				i++;
				//System.out.println(nums[i]+" " + str +" "+ i);
			}while (true);
			System.out.print("Numbers:");
			for(int j=0;j<i;j++){
				if(j != 0){
					System.out.print(",");
				}
			    System.out.print(nums.get(j));
			}
			System.out.println("");
			//System.out.println(method.list);

			int maxnum = nums.get(0);
			int minnum = nums.get(0);
			int total = nums.get(0);
			//System.out.println("total="+total);

			for (int j = 1; j < i; j++) {
				if(maxnum < nums.get(j)){
					maxnum = nums.get(j);
				}
				if(nums.get(j)<minnum){
					minnum = nums.get(j);
				}
				total = total + nums.get(j);
			}
			//System.out.println("total="+total);
			double averege = (double) (total / (double) i);
			//System.out.println("averege="+averege);

			double temp = 0.0;
			for (int j = 0; j < i; j++) {
				temp = temp + (nums.get(j) - averege) * (nums.get(j) - averege);
			}
			double sd = (double) (Math.sqrt(temp / i));

			System.out.println("The average is " + String.format("%.2f", averege) + ".");
			System.out.println("The minimum is " + minnum + ".");
			System.out.println("The maximum is " + maxnum + ".");
			System.out.println("The standard deviation is " + String.format("%.2f", sd) + ".");

	}
}
