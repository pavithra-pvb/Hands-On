import java.util.Arrays;

public class Exercise21 {
    public static void main(String[] args) {
        int[] arr1 = {1, 2, 3, 4, 5};
        modifyArray(arr1);
        System.out.println(Arrays.toString(arr1));
    }

    public static void modifyArray(int[] array) {
        array[0] = 10;
        array[1] = 20;
    }
}