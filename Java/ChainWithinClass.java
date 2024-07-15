/* Chain constructors in the same class */

public class ChainWithinClass
{
    ChainWithinClass() {
        System.out.println("\nThis is the no-arg constructor");
    }
    ChainWithinClass(int y) {
        this();
        int var1 = y;
        System.out.println("\nYou passed one argument: " + var1);
    }
    ChainWithinClass(int a, int b) {
        this(3);
        int var2 = a;
        int var3 = b;
        System.out.println("\nYou passed two arguments: " + var2 + " and " + var3);
    }
    public static void main(String[] args) {
        @SuppressWarnings("unused")
        ChainWithinClass chainObj = new ChainWithinClass(2,4);
    }
}