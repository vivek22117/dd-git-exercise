class ABCD
{
	private ABCD() {		
	}
	public static void test() {
		System.out.println("I am test method from utility class");
	}
	public static void show() {
		System.out.println("I am show method from utility class");
	}
}
public class index {
	public static void main(String[] args) {
		ABCD.test();
		ABCD.show();
	}
}
