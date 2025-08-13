public class GradeCalculator {

    public static void main(String[] args) {
        // --- Test Cases ---
        System.out.println("A score of 95 gets a grade of: " + getLetterGrade(95)); // Expected: "A"
        System.out.println("A score of 81 gets a grade of: " + getLetterGrade(81)); // Expected: "B"
        System.out.println("A score of 70 gets a grade of: " + getLetterGrade(70)); // Expected: "C"
        System.out.println("A score of 59 gets a grade of: " + getLetterGrade(59)); // Expected: "F"
        System.out.println("An invalid score of 105 gets: " + getLetterGrade(105)); // Expected: "Invalid score"


        
        
    }

    /**
     * Converts a numerical score to a letter grade.
     * 
     * @param score The numerical score (0-100).
     * @return The corresponding letter grade as a String.
     */
    public static String getLetterGrade(int score) {
        // Your implementation here
        if (score < 0 || score > 100) {
            return "Invalid score"; // Placeholder
        }

        switch (score / 10) {
            case 10: // score = 100    // if you are score = 100 the u are grade is "A"
            
            return "A+";
            case 9: // 90–99
                return "A";

            case 8: // 80–89
                return "B";

            case 7: // 70–79
                return "C";

            case 6: // 60–69
                return "D";

            default: // 0–59          // below 60 all are printing "F"
                return "F";

        }
    }
}
