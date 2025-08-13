
import javax.lang.model.util.ElementScanner14;

public class GradeCalculator {

    public static void main(String[] args) {
        // --- Test Cases ---
        System.out.println("A score of 95 gets a grade of: " + getLetterGrade(95)); // Expected: "A"
        System.out.println("A score of 81 gets a grade of: " + getLetterGrade(81)); // Expected: "B"
        System.out.println("A score of 70 gets a grade of: " + getLetterGrade(70)); // Expected: "C"
        System.out.println("A score of 59 gets a grade of: " + getLetterGrade(59)); // Expected: "F"
        // System.out.println("An invalid score of 105 gets: " + getLetterGrade(105));
        // // Expected: "Invalid score"
    }

    /**
     * Converts a numerical score to a letter grade.
     * 
     * @param score The numerical score (0-100).
     * @return The corresponding letter grade as a String.
     */
    public static String getLetterGrade(int score) {
        if (score < 0 || score > 100) {
            return "invalid";
           
        } else if (score >= 91 && score <= 100) {
           return "A";
        }
        else if (score >= 81 && score <= 90) {
           return "B";
        }
        else if (score >= 71 && score <= 80) {
           return "C";
        }
        else if (score >= 61 && score <= 80) {
           return "D";
        }
          else {
        return "F";
       }
        
        
        // return ""; // Placeholder

    // default:
    // System.out.println("this is invalid condition ");

    }
}
