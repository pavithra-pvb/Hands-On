public class Exercise23 {
    public static void main(String[] args) {
        int x = 0;
        
        while (x++ < 10) {}
        /* String message = x > 10 ? "Greater than" : false;*/ //error: incompatible types: bad type in conditional expression, boolean cannot be converted to String
        String message = x > 10 ? "Greater than" : String.valueOf(false);
        System.out.println("Message: " + message);
    }
}