import java.util.Scanner;

public class SimpleATM {

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
                    // Display the current balance
                    System.out.println("Your current balance is: Rs. " + balance);
                    break;

                case 2:
                    // Ask for a deposit amount and add it to the balance
                    System.out.print("Enter amount to deposit: ");
                    double depositAmount = scanner.nextDouble();
                    if (depositAmount > 0) {
                        balance += depositAmount;
                        System.out.println("Deposit successful! New balance: Rs. " + balance);
                    } else {
                        System.out.println("Invalid deposit amount.");
                    }
                    break;

                case 3:
                    // Ask for a withdrawal amount
                    System.out.print("Enter amount to withdraw: ");
                    double withdrawAmount = scanner.nextDouble();
                    if (withdrawAmount > 0 && withdrawAmount <= balance) {
                        balance -= withdrawAmount;
                        System.out.println("Withdrawal successful! New balance: Rs. " + balance);
                    } else if (withdrawAmount > balance) {
                        System.out.println("Insufficient balance.");
                    } else {
                        System.out.println("Invalid withdrawal amount.");
                    }
                    break;

                case 4:
                    // Exit the loop
                    isRunning = false;
                    System.out.println("Thank you for using Simple ATM. Goodbye!");
                    break;

                default:
                    // Handle invalid menu options
                    System.out.println("Invalid option. Please try again.");
                    break;
            }
        }

        scanner.close(); // Good practice to close the scanner
    }
}
