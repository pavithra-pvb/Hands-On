class One{

	public One(int x){
		System.out.print("int constructor");
	}

	public One(long l){
		System.out.print("long constructor");
	}
}

public class Exercise4{

	public static void main(String[] args){
		long l = 20L;
		One one = new One(l);
	}
}