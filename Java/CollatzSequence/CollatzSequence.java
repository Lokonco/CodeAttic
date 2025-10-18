/*
* The collatz sequence is a math problem
* it asks if repeating 2 simple arithmetic operations
* will return every positive number into 1
*/
import java.util.*;
public class CollatzSequence {
    public static void main(String[] args){
        Scanner input = new Scanner(System.in);
        //Ask for input and store
        System.out.println("Enter a number greater than 0");
        int num = input.nextInt();

        //Make sure input is valid
        while(true) {
            if (num <= 0) {
                System.out.println("Enter a number greater than 0");
                num = input.nextInt();
            } else {
                break;
            }
        }

        // Store user number
        int ogNum = num;
        System.out.println("Starting number is - " + ogNum);

        //Arithmetics & Logic
        int steps = 0;
        while (num != 1){
            steps++;
            if (num % 2 == 0){ // Even
                num = num / 2;
            } else { // Odd
                num = 3 * num + 1;
            }
            System.out.println("Current Number is - " + num);
        }
        // Print results
        System.out.println("Steps taken - " + steps + " / Starting number - " +ogNum + " / Steps taken - " + steps);
        input.close();
    }
}
