public class Exercise2 {
	public void print(Integer i) {
		System.out.println("Integer");
	}

	public void print(int i) {
		System.out.println("int");
	}

	public void print(long i) {
		System.out.println("long");
	}

	public static void main(String args[]) {
		Exercise2 test = new Exercise2();
		test.print(10);
	}
}