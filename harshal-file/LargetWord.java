public class LargetWord {
    public static String findLargestWord(String input) {
        String largest = "";
        StringBuilder currentWord = new StringBuilder();

        for (int i = 0; i < input.length(); i++) {
            char ch = input.charAt(i);

           
            if (Character.isLetter(ch)) {
                currentWord.append(ch);
            } else {
               
                if (currentWord.length() > largest.length()) {
                    largest = currentWord.toString();
                }
                currentWord.setLength(0); 
            }
        }

        return largest;
    }
    public static void main(String[] args) {
         String str = "fun&!! time2$3 !cat";
        System.out.println(findLargestWord("largest word is "+str));
    }
}
