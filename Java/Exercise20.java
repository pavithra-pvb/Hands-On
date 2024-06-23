public class Exercise20 {

    public static void main(String[] args) {
        try {
            methodA();
        } catch (RuntimeException e) {
            System.out.println("Caught RuntimeException in main method" );
        }
    }

    public static void methodA() {
        try {
            methodB();
        } catch (Exception e) {
            System.out.println("Caught Exception in methodA: ");
            throw new RuntimeException();
        } finally {
            System.out.println("methodA finally block");
        }
    }

    public static void methodB() throws Exception {
        try {
            throw new Exception();
        } finally {
            System.out.println("methodB finally block");
        }
    }
}