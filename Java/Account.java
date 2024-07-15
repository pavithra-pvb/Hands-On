/* Chain a constructor to another class */

class Account {
    Account(String first_name, int your_age) {
        String fname = first_name;
        int age = your_age;
        System.out.println("\nThe name entered is " + fname);
        System.out.println("\nYou are " + age + " years old.");
    }

    Account() {
        System.out.println("\nWelcome dear customer");
    }
    public static void main(String args[]) {
        @SuppressWarnings("unused")
        FixedDeposit acct = new FixedDeposit();
    }
}

class FixedDeposit extends Account {
    FixedDeposit() {
        super("Pavithra", 41); // calling the no-argument constructor in the base class
        double APY = 12.5;
        System.out.println("\nYour current interest rate is " + APY + "%");
    }
}