package mathinvestigationca1;

import java.util.Scanner;

public class ParabolaEquation {
    public static void main(String[] args) {
        Scanner input = new Scanner(System.in);

        // Get the x and y coordinates of three points
        System.out.print("Enter x1: ");
        double x1 = input.nextDouble();
        System.out.print("Enter y1: ");
        double y1 = input.nextDouble();
        System.out.print("Enter x2: ");
        double x2 = input.nextDouble();
        System.out.print("Enter y2: ");
        double y2 = input.nextDouble();
        System.out.print("Enter x3: ");
        double x3 = input.nextDouble();
        System.out.print("Enter y3: ");
        double y3 = input.nextDouble();

        // Solve the system of equations to find the coefficients of the parabolic equation
        double[][] matrix = {{x1*x1, x1, 1}, {x2*x2, x2, 1}, {x3*x3, x3, 1}};
        double[] vector = {y1, y2, y3};
        double[] solution = solveSystem(matrix, vector);

        // Output the equation of the parabola
        System.out.println("The equation of the parabola is: y = " + solution[0] + "x^2 + " + solution[1] + "x + " + solution[2]);
    }

    // Solves a system of linear equations using Gaussian elimination
    public static double[] solveSystem(double[][] matrix, double[] vector) {
        int n = vector.length;

        // Forward elimination
        for (int i = 0; i < n; i++) {
            double pivot = matrix[i][i];
            for (int j = i + 1; j < n; j++) {
                double factor = matrix[j][i] / pivot;
                vector[j] -= factor * vector[i];
                for (int k = i; k < n; k++) {
                    matrix[j][k] -= factor * matrix[i][k];
                }
            }
        }

        // Backward substitution
        double[] solution = new double[n];
        for (int i = n - 1; i >= 0; i--) {
            double sum = 0;
            for (int j = i + 1; j < n; j++) {
                sum += matrix[i][j] * solution[j];
            }
            solution[i] = (vector[i] - sum) / matrix[i][i];
        }

        return solution;
    }
}

