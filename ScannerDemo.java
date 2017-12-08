/**
 * @author Christelle
 * 
 * by Anisha Miah
 * 
 */
public class ScannerDemo {

	private static String file1 = "/Users/anishamiah/Downloads/ParserScannerOriginal/src/prog2.jay";
	private static int counter = 1;

	public static void main(String args[]) {

		TokenStream ts = new TokenStream(file1);

		System.out.println(file1);

		while (!ts.isEndofFile()) {
			Token a = ts.nextToken();
			System.out.println(a);
			
		
		}
	}
}
