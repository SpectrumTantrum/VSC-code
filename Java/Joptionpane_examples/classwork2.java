package Joptionpane_examples;
import javax.swing.JOptionPane;

public class classwork2 {
    public static void main(String[] args) {
    boolean option = true;
    while (option == true){
        String number1 = JOptionPane.showInputDialog(null, "What's your first number?");
        String number2 = JOptionPane.showInputDialog(null, "What's your second number?");
        int total = Integer.parseInt(number1) + Integer.parseInt(number2);
        JOptionPane.showMessageDialog(null, "The total is, " + total);

        int choice = JOptionPane.showConfirmDialog(null,"Do you want to continue?");
        if (choice == 1){                                        //Yes = 0 No = 1
            option = false;
            JOptionPane.showMessageDialog(null, "Thank you for using");
        }
    }
}
}
