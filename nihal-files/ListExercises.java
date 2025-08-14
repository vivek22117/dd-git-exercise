import java.util.ArrayList;
import java.util.List;

public class ListExercises {

    public static List<Integer> filterEvenNumbers(List<Integer> numbers) {
        // Your code here

         List<Integer> evenList = new ArrayList<>(); // Create new list for even numbers    
        for (Integer num : numbers) {
            if (num % 2 == 0) { // Check if even
                evenList.add(num);
            }
        }
        return evenList;
    
    }

    public static void main(String[] args) {
        List<Integer> myList = List.of(1, 2, 3, 4, 5, 6, 7, 8, 9, 10);
        List<Integer> evens = filterEvenNumbers(myList);
        System.out.println("Original List: " + myList);
        System.out.println("Even Numbers: " + evens);
        // Expected Output: Even Numbers: [2, 4, 6, 8, 10]
    }
}
