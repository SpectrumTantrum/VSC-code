package methodsquare;

import java.util.Scanner;

public class methodsquare {
    
    public static int square(int num){
        return (num * num);
    }

    /**
     * @param args
     */
    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in); //Create a scanner object
        System.out.println("Enter your number:");

        int number = myObj.nextInt(); //Read user input
        System.out.println("Your number squared is, " + square(number)); //Output user inpur
    }

}
