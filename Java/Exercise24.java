public class Exercise24 {
    private static int $;
    public static void main(String[] main) {
        //String a_b; compilation error due to an uninitialized variable
        String a_b = "Hello";
        System.out.print($);
        System.out.print("\n");
        //System.out.print(a_b); compilation error due to the attempt to print an uninitialized variable
        System.out.print(a_b);

    }
}