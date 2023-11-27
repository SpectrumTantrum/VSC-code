package employeeproject;

public class EmpTest {
    public static void main(String[] args) {
        Employee one = new Employee();
        one.first_name = "john";
        one.last_name = "doe";
        one.salary = 420.69;
        one.employee_id = 14;
        
        one.showEmp();
    }
}
