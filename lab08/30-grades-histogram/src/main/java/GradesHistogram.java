import java.io.*;
import java.util.*;
public class GradesHistogram {

//	public static void main(String[] argvs) throws IOException {
//		histogram("grades.in");
//	}

	public static void histogram(String fileName) throws IOException {
		BufferedReader f = new BufferedReader(new FileReader(fileName));
		String lines;
		int[] times = {0,0,0,0,0,0,0,0,0,0};

		ArrayList<Integer> list = new ArrayList<Integer>();

		String n = f.readLine();
		lines = f.readLine();
		while (lines != null) {
			String[] nums = lines.split(" ");
			for (String i : nums) {
				int x = Integer.parseInt(i);
				list.add(x);
				lines = f.readLine();
			}
		}
		System.out.print(" ");

		for (int i = 0; i <= 9; i++) {
			for (int j = 0; j < list.size(); j++) {
				if (list.get(j) >= (i * 10)) {
					if(list.get(j) < ((i + 1)) * 10){
					    times[i]++;
					}
				}
				if (list.get(j) == 100 & i==9) {
					times[i]++;
				}
			}
			//System.out.println(times[i]);

			if (i == 0) {
				System.out.print(i * 10 + " -  " + (i * 10 + 9) + ":");
				if(times[i] == 0){
					System.out.println("");
					continue;
				}
				while (times[i] > 0) {
					System.out.print("*");
					times[i]--;
				}
				System.out.println("");
			}

			if (i > 0 & i < 9) {
				System.out.print(i * 10 + " - " + (i * 10 + 9) + ":");
				if(times[i] == 0){
					System.out.println("");
					continue;
				}
				while (times[i] > 0) {
					System.out.print("*");
					times[i]--;
				}
				System.out.println("");
			}
		}
		System.out.print("90 -100:");

		while (times[9] > 0) {
			System.out.print("*");
			times[9]--;
		}

	}
}


