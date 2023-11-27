package employeeproject;

public class Employee {
    private String first_name;
    private String last_name;
    private double salary;
    private int employee_id;
    private static double minimum_wage = 16.00;
    private static int retirement_age = 65;

    public String getFirst_name(){
        return first_name;
    }

    public String getLast_name(){
        return last_name;
    }

    public double getSalary(){
        return salary;
    }

    public int getEmployee_id(){
        return employee_id;
    }

    public void setFirst_name(String first_name){
        this.first_name = first_name;
    }

    public void setLast_name(String last_name){
        this.last_name = last_name;
    }

    public void setSalary(double salary){
        this.salary = salary;
    }

    public void setEmployee_id(int employee_id){
        this.employee_id = employee_id;
    }

    public void showEmp(){
        System.out.println("Employee ID:" + employee_id);
        System.out.println("Name:" + first_name + " " + last_name);
        System.out.println("Salary: " + salary);
        System.out.println("Remember minimum wage and retirement age is " + minimum_wage + " and " + retirement_age);
    }
}
