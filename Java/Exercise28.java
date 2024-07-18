public class Exercise28 {
    public static void main(String[] args) {
        int y = 1; // error fix
        do { 
            //int y = 1;
            System.out.print(y++ + " "); 
        } while(y <= 10); // Error - cannot find symbol: variable y
   
    }
}