package Joptionpane_examples;

import javax.swing.JOptionPane;

public class example2 {
    public static void main(String[] args) {
        int choice = JOptionPane.showConfirmDialog(null,"Erase your hard disk?");
        if (choice == JOptionPane.YES_OPTION){                                        //Yes = 0 No = 1
            JOptionPane.showMessageDialog(null, "Disk erased!");
            JOptionPane.showMessageDialog(null, "just a joke lol");
        }
        else{
            JOptionPane.showMessageDialog(null, "Cancelled.");
        }
    }
}
