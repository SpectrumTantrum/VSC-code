package Joptionpane_examples;
import javax.swing.*;

public class example3 {
    public static void main(String[] args) {
        String name = JOptionPane.showInputDialog(null, "What's your name?");
        JOptionPane.showMessageDialog(null, "You have no bitches, " + name);
    }
}
