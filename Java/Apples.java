class Apples {
	{
	    System.out.println("\nThis is fresh from South Africa.");
	}
	
	Apples() {
		System.out.println("\nColor: Green");
	}
	
	{
		System.out.println("\nNo Artificial fertilisers used!");
	}
	
	Apples(String color) {
		System.out.println("Color: "+ color);
	}
	public static void main(String args[]) {
		@SuppressWarnings("unused")
		Apples myApple = new Apples();
	}
}
