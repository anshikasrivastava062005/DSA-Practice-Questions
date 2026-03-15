/* 7. Bela teaches her daughter to find the factors of a given number. When she provides a number to her
daughter, she should tell the factors of that number. Help her to do this, by writing a program. Write a
class FindFactor.java and write the main method in it.
Note:
If the input provided is negative, ignore the sign and provide the output. If the input is zero the output
should be “No Factors”.
Sample Input:-
54
Sample Output:-
1,2,3,6,9,18,27,54
*/

class FindFactor {

    public static void main(String[] args) {

        int num = 54;  // sample input

        // Ignore negative sign
        num = Math.abs(num);

        // If number is zero
        if (num == 0) {
            System.out.println("No Factors");
        } 
        else {

            boolean first = true;

            for (int i = 1; i <= num; i++) {
                if (num % i == 0) {

                    if (!first) {
                        System.out.print(",");
                    }

                    System.out.print(i);
                    first = false;
                }
            }
        }
    }
}