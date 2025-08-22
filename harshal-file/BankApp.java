
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
        else{
             System.out.println("withdrawal failed for " + accountHolderName + ". Insufficient funds or invalid amount!");
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

public class BankApp {
    public static void main(String[] args) {
        innerBankacount harshal = new innerBankacount("12345", "Harshal");
        innerBankacount nihal = new innerBankacount("67890", "Nihal");

        System.out.println(harshal.getAccountDetails());
        System.out.println(nihal.getAccountDetails());

         nihal.deposit(1000);      
        nihal.withdraw(1200);  
        
         harshal.deposit(10000);      
        harshal.withdraw(1200);  

         System.out.println("harshal amount will be "+harshal.getAccountDetails());
         System.out.println("nihal amount will be "+nihal.getAccountDetails());
       
    }
}
