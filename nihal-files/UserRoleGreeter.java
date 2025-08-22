public class UserRoleGreeter {

    public static String greetUser(String username, String userRole) {
         // 1. Extract the first name from fullName

        String firstName;
        if (username.contains(" ")) {
            firstName = username.split(" ")[0];
        } else {
            firstName = username;
        }
         // 2. Use a switch statement to find the permission level based on userRole
        String message = "";
        switch (userRole) {
            case "Admin":
                message = "Full Access";
                break;
            case "Editor":
                message = "Limited Access";
                break;
            case "Subscriber":
                message = "Read-Only Access";
                break;
            default:
                message = "Guest Access";
        }
      // 3. Use an if-else statement to print the final greeting
      
        String msg;
        if (message.equals("Full Access")) {
            msg = "Welcome, " + firstName + "! You have full administrative privileges.";
        } else if (message.equals("Limited Access")) {
            msg = "Welcome, " + firstName + "! You have permission to edit content.";
        } else if (message.equals("Read-Only Access")) {
            msg = "Welcome, " + firstName + "! You have permission to view content.";
        } else {
            msg = "Welcome, " + firstName + "! You have guest access.";
        }

        return msg;
    }

    public static void main(String[] args) {
        System.out.println(greetUser("Vivek Mishra", "Admin"));
        System.out.println(greetUser("Sonali Patil", "Editor"));
        System.out.println(greetUser("Nihal More", "Subscriber"));
        System.out.println(greetUser("Harshal Patil", "Developer"));
    }
}
