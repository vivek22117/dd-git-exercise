public class SimpleGreeter {

    public static void main(String[] args) {
        if (args.length > 0) {

            String name = args[0];
            System.out.println("Hello, " + name + "! Welcome to the command-line.");
        } else {
        
            System.out.println("Hello! Please provide a name as an argument to get a personalized greeting.");
            System.out.println("Example: java SimpleGreeter Nihal");
        }
    }
}
