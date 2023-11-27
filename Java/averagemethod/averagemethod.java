package averagemethod;

import java.util.Scanner;

public class averagemethod {
    
    public static double average(double a, double b){
       return (a + b) / 2.0; //Start here!
    }

    public static void main(String[] args) {
        Scanner myObj = new Scanner(System.in); //Create a scanner object
        System.out.println("Enter your number a:");
        double a = myObj.nextDouble(); //Read user input

        System.out.println("Enter your number b:");
        double b = myObj.nextDouble(); //Read user input

        
        System.out.println("Your average is, " + average(a, b));
    }

}
