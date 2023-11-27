//Write a java program to test if an array contains a specific value

package specificvalue;

import java.util.Scanner; // Import the Scanner class

public class specificvalue {

    public static void main(String[] args) {

        Scanner scan = new Scanner(System.in);

        System.out.print("Enter the number you want to find: ");

        int userinput = scan.nextInt();

        int array[] = {12, 34, 56, 76, 89, 42, 0, 2, 30};

        for (int count = 0; count < array.length; count++) {
            if(array[count] == userinput){
                System.out.println("Your number is found!");
            }
            else{
                System.out.println("Your number is not found!");

            }
        } 
    }
}
