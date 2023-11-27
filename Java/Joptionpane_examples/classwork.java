package Joptionpane_examples;
import javax.swing.JOptionPane;

public class classwork {
    public static void main(String[] args) {
        String celcius = JOptionPane.showInputDialog(null, "What is the celcius?");
        double farenheight = (Double.parseDouble(celcius) * 9 / 5) + 32;
        JOptionPane.showMessageDialog(null, "The temperature is, " + farenheight + " in farenheight");
    }
}
