import java.util.*;


class Exercise17 {

    public static void main(String[] args)

    {

        String countryArray[] = { "India", "Pakistan", "Afganistan"};


        List<String> countryList = new ArrayList<>();

        Collections.addAll(countryList, countryArray);


        System.out.println(countryList);

    }
}