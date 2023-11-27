package mathinvestigationca1;


import java.util.Scanner;

public class ProjectileVertex {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Pre-determined values
        double x0 = 0; // Starting point is the origin
        double y0 = 0; // Starting point is the origin
        double angle = 45; // Launch angle is 45 degrees
        double g = 9.81; // Gravitational acceleration is 9.81 m/s^2

        // Get the initial velocity
        System.out.print("Enter initial velocity: ");
        double v0 = input.nextDouble();

        // Convert the launch angle to radians
        double angleRadians = Math.toRadians(angle);

        // Calculate the initial horizontal and vertical velocities
        double v0x = v0 * Math.cos(angleRadians);
        double v0y = v0 * Math.sin(angleRadians);

        // Calculate the time it takes to reach the highest point
        double t_vertex = v0y / g;

        // Calculate the x and y coordinates of the vertex
        double x_vertex = x0 + v0x * t_vertex;
        double y_vertex = y0 + v0y * t_vertex - 0.5 * g * t_vertex * t_vertex;

        // Output the x and y coordinates of the vertex
        System.out.println("The vertex of the projectile motion trajectory is at (" + x_vertex + ", " + y_vertex + ")");
    }
}


