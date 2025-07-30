import java.util.Scanner;

class car {
    class Car {
    String brand;
    int year;

    Car(String b, int y) {
        brand = b;
        year = y;
    }

    void displayInfo() {
        System.out.println("Brand: " + brand + ", Year: " + year);
    }
}
public class Fact {
    public static void main(String[] args) {
        System.out.println("things went to above ");
         System.out.print("Enter first number: ");
        int a = scanner.nextInt();
        
        System.out.print("Enter second number: ");
        int b = scanner.nextInt();
        
        int sum = a + b;
        System.out.println("Sum: " + sum);
    }
}