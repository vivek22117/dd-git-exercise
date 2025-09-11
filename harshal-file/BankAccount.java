 class innerBankacount {
    // TODO: Define the private attributes: accountNumber, accountHolderName,
    // balance
    private String accountNumber;
    private String accountHolderName;
    private double balance;

    // TODO: Create the constructor to initialize the account
    public innerBankacount(String accNumber, String holderName) {
        this.accountNumber = accNumber;
        this.accountHolderName = holderName;
        this.balance = 0.0;
    }

    // TODO: Implement the deposit method
    public void deposit(double amount) {
        if (amount > 0) {
            balance += amount;
            System.out.println("updated balance is " + balance);
        }
    }

    // TODO: Implement the withdraw method
    public void withdraw(double amount) {
        if (amount > 0 && amount <= balance) {
            balance -= amount;
            System.out.println("remain balance after is " + balance);
        }
    }

    // TODO: Implement the getBalance method
    public double getBalance() {
        // Return the current balance

        return balance;
    }

    // TODO: Implement the getAccountDetails method
    public String getAccountDetails() {
        // Return a formatted string with all account details
        return "account number is  " + accountNumber +
                ", account Holder " + accountHolderName +
                ", balance " + balance;
    }
}

public class BankAccount {

    public static void main(String[] args) {
        innerBankacount ibc = new innerBankacount("12345","harshal");
        ibc.deposit(500);
        ibc.withdraw(200);

        System.out.println(ibc.getAccountDetails());
        System.out.println("Final Balance: " + ibc.getBalance());

    }
}