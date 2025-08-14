public class UserRoleGreeter {
    public static void greetUser(String username, String userRole) {
        // System.out.println("Processing user: " + username + " with role: " + userRole);
        // --- Your code starts here ---
        // 1. Extract the first name from fullName
         // String FirstName=username.
        String firstName;
        if (username.contains(" ")) {
            firstName = username.split(" ")[0];
        } else {
            firstName = username;
        }
       
        // 2. Use a switch statement to find the permission level based on userRole
        switch (userRole) {
            case "Admin":
                System.out.println("Admin-->Full Access");
                break;
            case "Editor":
                System.out.println("Editor-->Limited Access");
                break;
            case "Subscriber":
                System.out.println("Subscriber-->Read-Only Access");
                break;
            case "Developer":
                System.out.println("Developer-->Guest Access");
                break;
            default:
                System.out.println("invalid input");
        }
        // 3. Use an if-else statement to print the final greeting
        if (userRole != null) {
            System.out.println("Welcome, " + firstName + "! You have " + userRole + ".");
        } 
        // --- Your code ends here ---
       
    }

    public static void main(String[] args) {
        greetUser("Vivek Mishra", "Admin");
        greetUser("sonali", "Editor");
        greetUser("nihal", "Subscriber");
        greetUser("harshal", "Developer");
        // System.out.println(greetMessage);
        // Expected Output: "Welcome, Ada! You have full administrative privileges."

    }
}
