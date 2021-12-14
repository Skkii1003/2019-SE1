import java.io.*;

public class CurrencyCalculation {

	public static void main(String[] args) {
		double euros;
		double rate;
		double dollars;
		System.out.println("How many euros are you exchanging?");
		try {
			BufferedReader reader = new BufferedReader(new InputStreamReader(System.in));
			euros = Double.parseDouble(reader.readLine());
			System.out.println("What is the exchange rate?");
			rate = Double.parseDouble(reader.readLine());
			dollars = euros*rate/100;
			String result = "";
			result = result.format("%.2f euros at an exchange rate of %.2f is %.2f U.S. dollars.",euros,rate,dollars);
			System.out.println(result);
		}catch(IOException ex){
			ex.printStackTrace();
		}
	}

}
