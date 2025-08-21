import java.util.Scanner;

public class SimpleAtm {

    public static void main(String[] args) {
        // 1. Initialize variables
        double balance = 1000.00; // Starting balance
        boolean isRunning = true; // Controls the main loop
        Scanner scanner = new Scanner(System.in);

        // 2. Create the main loop that runs as long as isRunning is true
        while (isRunning) {
            // Display the menu
            System.out.println("\n--- Welcome to Simple ATM ---");
            System.out.println("1: Check Balance");
            System.out.println("2: Deposit Money");
            System.out.println("3: Withdraw Money");
            System.out.println("4: Exit");
            System.out.print("Please choose an option: ");

            int choice = scanner.nextInt();

            // 3. Use a switch statement to handle the user's choice
            switch (choice) {
                case 1:
                    // TODO: Display the current balance
                    System.out.println("Your Current Balance is " + balance);
                    break;
                case 2:
                    // TODO: Ask for a deposit amount and add it to the balance
                    long depositMoney = scanner.nextLong();
                    if (depositMoney > 0 && depositMoney <= balance) {
                        System.out.println("before withdrawn" + balance);
                        depositMoney += balance;
                        System.out.println("total amount is " + depositMoney);
                        System.out.println("Avalilable balance is " + balance);
                    }
                    break;
                case 3:
                    // TODO: Ask for a withdrawal amount
                    // Use an if-else statement to check for sufficient funds
                    System.out.print("Enter amount to withdraw: ₹");
                    double withdrawAmount = scanner.nextDouble();
                    if (withdrawAmount > 0 && withdrawAmount <= balance) {
                        withdrawAmount = balance - withdrawAmount;
                        System.out.println("remaning amount is " + withdrawAmount);

                    } else if (withdrawAmount > balance) {
                        System.out.println("insufficient amount is " + withdrawAmount);
                    } else {
                        System.out.println("invalid amount ");
                    }
                    break;
                case 4:
                    // TODO: Set isRunning to false to exit the loop and print a goodbye message
                    System.out.println("thank for visit come again ");
                    isRunning = false;
                    break;
                default:

                    // TODO: Handle invalid menu options
                    System.out.println("You Chose InValid Option");
                    break;
            }
        }

        scanner.close(); // Good practice to close the scanner
    }
}
