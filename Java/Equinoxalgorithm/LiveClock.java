package Equinoxalgorithm;

import java.awt.FlowLayout;
import java.awt.Font;
import java.time.LocalTime;
import java.time.ZoneId;
import java.time.format.DateTimeFormatter;

import javax.swing.JFrame;
import javax.swing.JLabel;

public class LiveClock extends JFrame implements Runnable {
    private JLabel label;

    public LiveClock() {
        // Set up the window
        setTitle("Live Clock");
        setSize(300, 100);
        setResizable(false);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
        setLayout(new FlowLayout(FlowLayout.CENTER, 10, 20));

        // Add the label for the time
        label = new JLabel();
        label.setFont(new Font("Arial", Font.BOLD, 32)); // Set the font size to 24
        add(label);

        // Start the clock
        new Thread(this).start();
    }

    @Override
    public void run() {
        while (true) {
            // Get the current time in GMT+8
            LocalTime time = LocalTime.now(ZoneId.of("GMT+8"));

            // Format the time as HH:mm:ss
            DateTimeFormatter formatter = DateTimeFormatter.ofPattern("HH:mm:ss");
            String formattedTime = time.format(formatter);

            // Update the label
            label.setText(formattedTime);

            // Wait for one second
            try {
                Thread.sleep(1000);
            } catch (InterruptedException e) {
                e.printStackTrace();
            }
        }
    }

    public static void main(String[] args) {
        // Create the clock window
        LiveClock clock = new LiveClock();
        clock.setVisible(true);
    }
}

