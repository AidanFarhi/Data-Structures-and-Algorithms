package InterviewProblems.IsPalindrome;

/*
Problem:
Check if a string is a palindrome or not.
Ex) is_palindrome(level) -> True | is_palindrome(levels) -> False
*/

public class IsPalindrome {

    public static boolean isPalindrome(String str) {
        int i = 0;
        int j = str.length() - 1;
        while (i <= j) {
            if (str.charAt(i) != str.charAt(j)) return false;
            ++i;
            --j;
        }
        return true;
    }

    // Test Client
    public static void main(String[] args) {
        String test1 = "level";
        String test2 = "levels";
        System.out.println("level: " + IsPalindrome.isPalindrome(test1));
        System.out.println("levels: " + IsPalindrome.isPalindrome(test2));
    }
}