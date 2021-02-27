package InterviewProblems.ReverseInteger;

/*
Problem:
Reverse a positive integer. 
Can you do it without using an additional data structure (arr, string, ect..)?
ex) 1234 -> 4321
*/

public class ReverseInteger {

    public static int reverseInt(int num) {
        int res = 0;
        while (num > 0) {
            int rem = num % 10;
            num /= 10;
            res = res * 10 + rem;
        }
        return res;
    }

    public static void main(String[] args) {
        System.out.println(ReverseInteger.reverseInt(1234));
        System.out.println(ReverseInteger.reverseInt(100014));
        System.out.println(ReverseInteger.reverseInt(2526));
        System.out.println(ReverseInteger.reverseInt(5166));
    }
}