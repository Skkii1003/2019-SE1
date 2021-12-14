
import static org.junit.Assert.assertEquals;

import java.io.BufferedWriter;
import java.io.ByteArrayOutputStream;
import java.io.FileNotFoundException;
import java.io.FileWriter;
import java.io.IOException;
import java.io.PrintStream;

import org.junit.After;
import org.junit.Before;
import org.junit.Test;

public class GradesHistogramTest {
	PrintStream console = null;
	ByteArrayOutputStream bytes = null;
	String lineBreak = null;
	String filePath = "grades.in";

	@Before
	public void setUp() throws Exception {
		bytes = new ByteArrayOutputStream();
		console = System.out;
		System.setOut(new PrintStream(bytes));
		lineBreak = System.getProperty("line.separator");
	}

	@After 
	public void tearDown() throws Exception {
		System.setOut(console);
	}
	
	@Test
	public void testHistogram1() throws IOException {
		BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
		writer.append("2"+lineBreak);
		writer.append("4 99");
		writer.flush();
		writer.close();
		String s=" 0 -  9:*"+lineBreak
				+"10 - 19:"+lineBreak
				+"20 - 29:"+lineBreak
				+"30 - 39:"+lineBreak
				+"40 - 49:"+lineBreak
				+"50 - 59:"+lineBreak
				+"60 - 69:"+lineBreak
				+"70 - 79:"+lineBreak
				+"80 - 89:"+lineBreak
				+"90 -100:*";
		
		GradesHistogram.histogram(filePath);
		assertEquals(s,bytes.toString());
		
	}
	
	@Test
	public void testHistogram2() throws IOException {
		BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
		writer.append("5"+lineBreak);
		writer.append("14 24 56 21 87");
		writer.flush();
		writer.close();
		String s=" 0 -  9:"+lineBreak
				+"10 - 19:*"+lineBreak
				+"20 - 29:**"+lineBreak
				+"30 - 39:"+lineBreak
				+"40 - 49:"+lineBreak
				+"50 - 59:*"+lineBreak
				+"60 - 69:"+lineBreak
				+"70 - 79:"+lineBreak
				+"80 - 89:*"+lineBreak
				+"90 -100:";
		
		GradesHistogram.histogram(filePath);
		assertEquals(s,bytes.toString());
		
	}
	
	@Test
	public void testHistogram3() throws IOException {
		BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
		writer.append("9"+lineBreak);
		writer.append("34 32 45 76 92 12 34 0 23");
		writer.flush();
		writer.close();
		String s=" 0 -  9:*"+lineBreak
				+"10 - 19:*"+lineBreak
				+"20 - 29:*"+lineBreak
				+"30 - 39:***"+lineBreak
				+"40 - 49:*"+lineBreak
				+"50 - 59:"+lineBreak
				+"60 - 69:"+lineBreak
				+"70 - 79:*"+lineBreak
				+"80 - 89:"+lineBreak
				+"90 -100:*";
		
		GradesHistogram.histogram(filePath);
		assertEquals(s,bytes.toString());
		
	}
	
	@Test
	public void testHistogram4() throws IOException {
		BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
		writer.append("12"+lineBreak);
		writer.append("0 21 3 34 76 32 45 87 93 23 93 42");
		writer.flush();
		writer.close();
		String s=" 0 -  9:**"+lineBreak
				+"10 - 19:"+lineBreak
				+"20 - 29:**"+lineBreak
				+"30 - 39:**"+lineBreak
				+"40 - 49:**"+lineBreak
				+"50 - 59:"+lineBreak
				+"60 - 69:"+lineBreak
				+"70 - 79:*"+lineBreak
				+"80 - 89:*"+lineBreak
				+"90 -100:**";
		
		GradesHistogram.histogram(filePath);
		assertEquals(s,bytes.toString());
		
	}
	
	@Test
	public void testHistogram5() throws IOException {
		BufferedWriter writer = new BufferedWriter(new FileWriter(filePath));
		writer.append("15"+lineBreak);
		writer.append("49 50 51 59 0 5 9 10 15 19 50 55 89 99 100");
		writer.flush();
		writer.close();
		String s=" 0 -  9:***"+lineBreak
				+"10 - 19:***"+lineBreak
				+"20 - 29:"+lineBreak
				+"30 - 39:"+lineBreak
				+"40 - 49:*"+lineBreak
				+"50 - 59:*****"+lineBreak
				+"60 - 69:"+lineBreak
				+"70 - 79:"+lineBreak
				+"80 - 89:*"+lineBreak
				+"90 -100:**";
		
		GradesHistogram.histogram(filePath);
		assertEquals(s,bytes.toString());
	}

}
