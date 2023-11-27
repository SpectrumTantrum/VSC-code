
/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/Classes/Main.java to edit this template
 */
package EvenOrOdd;

import java.util.Scanner;

public class EvenOrOdd {

    public static void main(String[] args) {
        // Check Whether a Given Number is Even or Odd

        Scanner input = new Scanner(System.in);
        System.out.print("What is your number? ");
        int number = input.nextInt();
                
        if (number % 2 == 0) {
            System.out.print("The Number is even.");
        }
        
        else{
            System.out.print("The Number is odd" );
    }
    }
    
    
}
