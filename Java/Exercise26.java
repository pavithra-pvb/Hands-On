public class Exercise26 {
    public static void main(String[] args) {
        int x1 = 50, x2 = 75;
        boolean b = x1 >= x2;
        /* if(b = true) */ // using the assignment operator = instead of the equality operator ==.
        if(b == true) // bug fix
            System.out.println("Success");
        else
            System.out.println("Failure");
    }
}