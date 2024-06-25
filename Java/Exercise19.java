public class Exercise19 {
    public static void main(String[] args) {

        try {
            method();
        } catch (Exception e) {
            System.out.println("Exception caught in main");
        } finally {
            System.out.println("Finally block executed");
        }
    }

    static void method() {
        try {
            throw new RuntimeException("Exception in method");
        } finally {
            System.out.println("Finally block in method");
        }
    }
}