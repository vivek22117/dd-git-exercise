package Constructors;

public class BankApp {
    public static void main(String[] args) {
        
        //  Create a BankAccount object for a person named

        BankAccount Nihal = new BankAccount("10001", "Nihal More");
        BankAccount Harshal = new BankAccount("10002", "Harshal Patil");
        BankAccount Damini = new BankAccount("10003", "Damini Patil");
        BankAccount Sonali = new BankAccount("10004", "Sonali Patil");
        BankAccount Abhishak = new BankAccount("10005", "Abhishak Patil");

        

        System.out.println("--- Initial Account States ---");
        //  Print initial details for both accounts
        System.out.println(Nihal.getAccountDetails());
        System.out.println("--------------------------------------------");
        System.out.println(Harshal.getAccountDetails());
        System.out.println("--------------------------------------------");
        System.out.println(Damini.getAccountDetails());
        System.out.println("--------------------------------------------");
        System.out.println(Abhishak.getAccountDetails());
        System.out.println("--------------------------------------------");
        System.out.println(Sonali.getAccountDetails());
        System.out.println("--------------------------------------------");
        

        System.out.println("\n--- Performing Transactions for Harshal---");
        //  Deposit $500 into Harshal's account
        Harshal.deposit(500);
        //  Withdraw $200 from Harshal's account
        Harshal.withdraw(200);

        System.out.println("\n--- Performing Transactions for Nihal---");
        //  Deposit $1000 into Nihal's account
        Nihal.deposit(1000);
        //  Attempt to withdraw $1200 from Nihal's account (should fail)
        Nihal.withdraw(1200);

        System.out.println("\n--- Final Account States ---");
        
        //  Print final details for both accounts

        System.out.println(Harshal.getAccountDetails());
        System.out.println("----------------------------------------------");
        System.out.println(Nihal.getAccountDetails());
        System.out.println("----------------------------------------------");
    }
}
