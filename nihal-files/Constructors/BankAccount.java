package Constructors;

public class BankAccount {
    // Define the private attributes
    private String accountNumber;
    private String accountHolderName;
    private double balance;

    // Create the constructor to initialize the account
    public BankAccount(String accountNumber, String nameofAccountholder) {
        this.accountNumber = accountNumber;
        this.accountHolderName = nameofAccountholder;
        this.balance = 0.0;
    }
    // Deposit Method
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;

            System.out.println("Deposite : Rs." + amount);
        } else {
            System.out.println("Invalid deposite amount");
        }
    }
      // Withdraw method
    public void withdraw(double amount) {
        if (amount <= 0) {
            System.out.println("Invalid amount");
        } else if (amount > balance) {
            System.out.println("Insifficient funds....");
        } else {
            balance -= amount;
            System.out.println("Withdraw Rs : " + amount);
        }
    }
          // Get Balance method  
    public double getBalance() {
        return balance;
    }
       // get account Details method
    public String getAccountDetails() {
        return "Account Number: " + accountNumber +
                "\nAccount Holder: " + accountHolderName +
                "\nBalance: Rs." + balance;
    }
}
