
public class CurrencyCalculation {

	public static void main(String[] args) {
		double euros = 0.0d;
		double exchangerate = 0.0d;
		double dollars = 0.0d;
		String string1 = null;
		String string2 = null;

		BufferedReader br=new BufferedReader(new InputStreamReader(System.in));

		System.out.println("How many euros are you exchanging?");
		string1 = br.readline();

		System.out.println("What is the exchange rate?");
		string2 = br.readline();

		euros = Double.parseDouble(string1);
		exchangerate = Double.parseDouble(string2);

		dollars = euros / 100 * exchangerate;

		System.out.printf("%.2f euros at an exchange rate of %.2f is %.2f U.S. dollars.",euros,exchangerate,dollars);
	}

}
